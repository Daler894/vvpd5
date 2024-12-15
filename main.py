import math


def calculate_ex(x, iterations=10):
    """
    Вычисление экспоненты e^x с использованием ряда Тейлора.

    Аргументы:
    x -- значение для вычисления e^x
    iterations -- количество итераций для точности (по умолчанию 10)

    Возвращает:
    Значение e^x
    """
    result = 0
    for n in range(iterations):
        result += x**n / math.factorial(n)
    return result


def calculate_sh(x, iterations=10):
    """
    Вычисление гиперболического синуса sh(x) с использованием ряда Тейлора.

    Аргументы:
    x -- значение для вычисления sh(x)
    iterations -- количество итераций для точности (по умолчанию 10)

    Возвращает:
    Значение sh(x)
    """
    result = 0
    for n in range(iterations):
        result += x**(2*n+1) / math.factorial(2*n+1)
    return result