import sympy as sp
from IPython.display import display, Latex


def display_function(func_name, func):
    """Выводит на экран функцию"""
    display(Latex("${} = {}$".format(sp.latex(func_name), sp.latex(func))))


def display_function_with_some_result(func_name, func, result_name, result):
    """Выводит на экран функцию с каким-либо результатом, связанный с функцией"""
    display(Latex(
        "${} = {}$".format(sp.latex(func_name), sp.latex(func))),
    Latex('${}: {}$'.format(sp.latex(result_name), sp.latex(result))))
