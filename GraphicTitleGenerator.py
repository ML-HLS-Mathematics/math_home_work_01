def generate_function_title(func_name):
    """Возвращает строку со стартовым заголовком для графика фнукции"""
    return f'График функции {func_name}'


def generate_extr_points_title(func_name):
    """Возвращает строку с заголовком для графика, где будут отображаться точки экстремумов"""
    return f'График функции {generate_function_title(func_name)} с точками экстремумов'


def generate_extr_and_infl_points_title(func_name):
    """Возвращает строку с заголовком для графика, где будут отображаться точки экстремумов и точки перегибов"""
    return f'{generate_extr_points_title(func_name)} и точками перегибов'


def generate_minimum_gradient_title(func_name):
    """Возвращает строку с заголовком для графика, где будет отображаться точка минимума функции,
    найденная с помощью градиентного спуска"""
    return f'{generate_function_title(func_name)} с наименьшей точкой минимума функции, найденной с помощью градиентного спуска'

def generate_minimum_newton_title(func_name):
    """Возвращает строку с заголовком для графика, где будет отображаться точка минимума функции,
    найденная с помощью метода Ньютона"""
    return f'{generate_function_title(func_name)} с точкой минимума минимума функции, найденной с помощью метода Ньютона'
