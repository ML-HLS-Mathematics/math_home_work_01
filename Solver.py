import sympy as sp


def solve_function_multiple(func, args):
    return [func(x) for x in args]


def solve_function(func):
    """Возвращает все решения уравнения функции, включая комплексные"""
    return sp.solve(func)


def solve_with_only_reals(func):
    """Возвращает все действительные решения уравнения функции"""
    return [sp.Float(sp.simplify(x)) for x in sp.solveset(func, domain=sp.Reals)]
