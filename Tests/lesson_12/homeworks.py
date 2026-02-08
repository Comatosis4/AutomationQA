def sum_numbers(string):
    """функція розбиває стрінгу по ',' і повертає суму розбитих чисел, якщо всередині нема відмінних від чисел символів
    :param string: функція приймає стрінгу
    :return: повертає суму чисел або помилку якщо є сторонні символи
    """
    try:
        numbers = string.split(",")
        n = 0
        for num in numbers:
            n += int(num)
        return n
    except ValueError:
        return 'Не числове значення'


def part_payment(part, month: int):
    """Функція розраховує повну вартість товару при оплаті частинами

    :param part: вказати місячну плату
    :param month: вказати кількість місяців для оплати
    :return: повертає ціну за товар
    """
    if part <= 0 or month <= 0:
        return 'Wrong data'
    elif isinstance(month, float):
        return 'Month cant be float'

    return part * month

def even_numbers(numbers: list) -> int:
    """Функція приймає ліст з числами і повертає суму парних чисел в ньому

    :param numbers: введіть ліст  з числами
    :return: повертає суму парних чисел
    """
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    return sum

class Figure:
    def perimeter(self):
        pass
    def area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side**2
    def perimeter(self):
        return self.__side*4