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

def main():
    """
    Основное меню программы.
    """
    while True:
        print("\nМеню программы:")
        print("1. Вычислить e^x")
        print("2. Вычислить sh(x)")
        print("3. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                x = float(input("Введите значение x для e^x: "))
                print(f"Результат: e^{x} = {calculate_ex(x)}")
            except ValueError:
                print("Ошибка: введите корректное число!")
        elif choice == "2":
            try:
                x = float(input("Введите значение x для sh(x): "))
                print(f"Результат: sh({x}) = {calculate_sh(x)}")
            except ValueError:
                print("Ошибка: введите корректное число!")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите корректный номер действия!")


if __name__ == "__main__":
    main()