import itertools
import logging
import warnings
from typing import List, NamedTuple, Optional, Sequence, Tuple

import cvxpy as cp
import numpy as np
from numpy.typing import NDArray

from pydvl.utils import MapReduceJob, ParallelConfig, Status, Utility
from pydvl.value import ValuationResult

__all__ = [
    "_solve_least_core_linear_program",
    "_solve_egalitarian_least_core_quadratic_program",
    "lc_solve_problem",
    "lc_solve_problems",
    "LeastCoreProblem",
]

logger = logging.getLogger(__name__)

LeastCoreProblem = NamedTuple(
    "LeastCoreProblem",
    [("utility_values", NDArray[np.float_]), ("A_lb", NDArray[np.float_])],
)


def lc_solve_problem(
    problem: LeastCoreProblem, *, u: Utility, algorithm: str, **options
) -> ValuationResult:
    """Solves a linear problem prepared by :func:`mclc_prepare_problem`.
    Useful for parallel execution of multiple experiments by running this as a
    remote task.

    See :func:`~pydvl.value.least_core.naive.exact_least_core` or
    :func:`~pydvl.value.least_core.montecarlo.montecarlo_least_core` for
    argument descriptions.
    """
    n = len(u.data)

    if np.any(np.isnan(problem.utility_values)):
        warnings.warn(
            f"Calculation returned "
            f"{np.sum(np.isnan(problem.utility_values))} NaN "
            f"values out of {problem.utility_values.size}",
            RuntimeWarning,
        )

    logger.debug("Removing possible duplicate values in lower bound array")
    b_lb = problem.utility_values
    A_lb, unique_indices = np.unique(problem.A_lb, return_index=True, axis=0)
    b_lb = b_lb[unique_indices]

    logger.debug("Building equality constraint")
    A_eq = np.ones((1, n))
    # We might have already computed the total utility. That's the index of the
    # row in A_lb with all ones.
    total_utility_index = np.where(A_lb.sum(axis=1) == n)[0]
    if len(total_utility_index) == 0:
        b_eq = np.array([u(u.data.indices)])
    else:
        b_eq = b_lb[total_utility_index]

    _, subsidy = _solve_least_core_linear_program(
        A_eq=A_eq, b_eq=b_eq, A_lb=A_lb, b_lb=b_lb, **options
    )

    values: Optional[NDArray[np.float_]]

    if subsidy is None:
        logger.debug("No values were found")
        status = Status.Failed
        values = np.empty(n)
        values[:] = np.nan
        subsidy = np.nan
    else:
        values = _solve_egalitarian_least_core_quadratic_program(
            subsidy,
            A_eq=A_eq,
            b_eq=b_eq,
            A_lb=A_lb,
            b_lb=b_lb,
            **options,
        )

        if values is None:
            logger.debug("No values were found")
            status = Status.Failed
            values = np.empty(n)
            values[:] = np.nan
            subsidy = np.nan
        else:
            status = Status.Converged

    return ValuationResult(
        algorithm=algorithm,
        status=status,
        values=values,
        subsidy=subsidy,
        stderr=None,
        data_names=u.data.data_names,
    )


def lc_solve_problems(
    problems: Sequence[LeastCoreProblem],
    u: Utility,
    algorithm: str,
    config: ParallelConfig = ParallelConfig(),
    n_jobs: int = 1,
    **options,
) -> List[ValuationResult]:
    """Solves a list of linear problems in parallel.

    :param u: Utility.
    :param problems: Least Core problems to solve, as returned by
        :func:`~pydvl.value.least_core.montecarlo.mclc_prepare_problem`.
    :param algorithm: Name of the valuation algorithm.
    :param config: Object configuring parallel computation, with cluster
        address, number of cpus, etc.
    :param n_jobs: Number of parallel jobs to run.
    :param options: Additional options to pass to the solver.
    :return: List of solutions.
    """

    def _map_func(
        problems: List[LeastCoreProblem], *args, **kwargs
    ) -> List[ValuationResult]:
        return [lc_solve_problem(p, *args, **kwargs) for p in problems]

    map_reduce_job: MapReduceJob[
        "LeastCoreProblem", "List[ValuationResult]"
    ] = MapReduceJob(
        inputs=problems,
        map_func=_map_func,
        map_kwargs=dict(u=u, algorithm=algorithm, **options),
        reduce_func=lambda x: list(itertools.chain(*x)),
        config=config,
        n_jobs=n_jobs,
    )
    solutions = map_reduce_job()

    return solutions


def _solve_least_core_linear_program(
    A_eq: NDArray[np.float_],
    b_eq: NDArray[np.float_],
    A_lb: NDArray[np.float_],
    b_lb: NDArray[np.float_],
    **options,
) -> Tuple[Optional[NDArray[np.float_]], Optional[float]]:
    """Solves the Least Core's linear program using cvxopt.

    .. math::

        \text{minimize} \ & e \\
        \mbox{such that} \ & A_{eq} x = b_{eq}, \\
        & A_{lb} x + e \ge b_{lb},\\
        & A_{eq} x = b_{eq},\\
        & x in \mathcal{R}^n , \\
        & e \ge 0

     where :math:`x` is a vector of decision variables; ,
    :math:`b_{ub}`, :math:`b_{eq}`, :math:`l`, and :math:`u` are vectors; and
    :math:`A_{ub}` and :math:`A_{eq}` are matrices.

    :param A_eq: The equality constraint matrix. Each row of ``A_eq`` specifies the
        coefficients of a linear equality constraint on ``x``.
    :param b_eq: The equality constraint vector. Each element of ``A_eq @ x`` must equal
        the corresponding element of ``b_eq``.
    :param A_lb: The inequality constraint matrix. Each row of ``A_lb`` specifies the
        coefficients of a linear inequality constraint on ``x``.
    :param b_lb: The inequality constraint vector. Each element represents a
        lower bound on the corresponding value of ``A_lb @ x``.
    :param options: Keyword arguments that will be used to select a solver
        and to configure it. For all possible options, refer to `cvxpy's documentation
        <https://www.cvxpy.org/tutorial/advanced/index.html#setting-solver-options>`_
    """
    logger.debug(f"Solving linear program : {A_eq=}, {b_eq=}, {A_lb=}, {b_lb=}")

    n_variables = A_eq.shape[1]

    x = cp.Variable(n_variables)
    e = cp.Variable()

    objective = cp.Minimize(e)
    constraints = [
        e >= 0,
        A_eq @ x == b_eq,
        (A_lb @ x + e * np.ones(len(A_lb))) >= b_lb,
    ]
    problem = cp.Problem(objective, constraints)

    solver = options.pop("solver", cp.ECOS)

    try:
        problem.solve(solver=solver, **options)
    except cp.error.SolverError as err:
        raise ValueError("Could not solve linear program") from err

    if problem.status in cp.settings.SOLUTION_PRESENT:
        logger.debug("Problem was solved")
        if problem.status in [cp.settings.OPTIMAL_INACCURATE, cp.settings.USER_LIMIT]:
            warnings.warn(
                "Solver terminated early. Consider increasing the solver's "
                "maximum number of iterations in options",
                RuntimeWarning,
            )
        subsidy = e.value.item()
        # HACK: sometimes the returned least core subsidy
        # is negative but very close to 0
        # to avoid any problems with the subsequent quadratic program
        # we just set it to 0.0
        if subsidy < 0:
            warnings.warn(
                f"Least core subsidy e={subsidy} is negative but close to zero. "
                "It will be set to 0.0",
                RuntimeWarning,
            )
            subsidy = 0.0
        return x.value, subsidy

    if problem.status in cp.settings.INF_OR_UNB:
        warnings.warn(
            "Could not find solution due to infeasibility or unboundedness of problem.",
            RuntimeWarning,
        )
    return None, None


def _solve_egalitarian_least_core_quadratic_program(
    subsidy: float,
    A_eq: NDArray[np.float_],
    b_eq: NDArray[np.float_],
    A_lb: NDArray[np.float_],
    b_lb: NDArray[np.float_],
    **options,
) -> Optional[NDArray[np.float_]]:
    """Solves the egalitarian Least Core's quadratic program using cvxopt.

    .. math::

        \text{minimize} \ & \| x \|_2 \\
        \mbox{such that} \ & A_{eq} x = b_{eq}, \\
        & A_{lb} x + e \ge b_{lb},\\
        & A_{eq} x = b_{eq},\\
        & x in \mathcal{R}^n , \\
        & e \text{ is a constant.}

     where :math:`x` is a vector of decision variables; ,
    :math:`b_{ub}`, :math:`b_{eq}`, :math:`l`, and :math:`u` are vectors; and
    :math:`A_{ub}` and :math:`A_{eq}` are matrices.

    :param subsidy: Minimal subsidy returned by :func:`_solve_least_core_linear_program`
    :param A_eq: The equality constraint matrix. Each row of ``A_eq`` specifies the
        coefficients of a linear equality constraint on ``x``.
    :param b_eq: The equality constraint vector. Each element of ``A_eq @ x`` must equal
        the corresponding element of ``b_eq``.
    :param A_lb: The inequality constraint matrix. Each row of ``A_lb`` specifies the
        coefficients of a linear inequality constraint on ``x``.
    :param b_lb: The inequality constraint vector. Each element represents a
        lower bound on the corresponding value of ``A_lb @ x``.
    :param options: Keyword arguments that will be used to select a solver
        and to configure it. Refer to the following page for all possible options:
        https://www.cvxpy.org/tutorial/advanced/index.html#setting-solver-options
    """
    logger.debug(f"Solving quadratic program : {A_eq=}, {b_eq=}, {A_lb=}, {b_lb=}")

    if subsidy < 0:
        raise ValueError("The least core subsidy must be non-negative.")

    n_variables = A_eq.shape[1]

    x = cp.Variable(n_variables)

    objective = cp.Minimize(cp.norm2(x))
    constraints = [
        A_eq @ x == b_eq,
        (A_lb @ x + subsidy * np.ones(len(A_lb))) >= b_lb,
    ]
    problem = cp.Problem(objective, constraints)

    solver = options.pop("solver", cp.ECOS)

    try:
        problem.solve(solver=solver, **options)
    except cp.error.SolverError as err:
        raise ValueError("Could not solve quadratic program") from err

    if problem.status in cp.settings.SOLUTION_PRESENT:
        logger.debug("Problem was solved")
        if problem.status in [cp.settings.OPTIMAL_INACCURATE, cp.settings.USER_LIMIT]:
            warnings.warn(
                "Solver terminated early. Consider increasing the solver's "
                "maximum number of iterations in options",
                RuntimeWarning,
            )
        return x.value  # type: ignore

    if problem.status in cp.settings.INF_OR_UNB:
        warnings.warn(
            "Could not find solution due to infeasibility or unboundedness of problem.",
            RuntimeWarning,
        )
    return None
