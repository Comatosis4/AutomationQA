print('-' * 15)
print('Task 1')

""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 9:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f'{str(number)} x {str(multiplier)} = {str(result)}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24

# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""
print('-' * 15)
print('Task 2')

def sum_of_two(x: int, y: int) -> int:
    return x + y
print(sum_of_two(5, 3))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел."""
print('-' * 15)
print('Task 3')

def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)
print(average([1, 7, 12.5, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""
print('-' * 15)
print('Task 4')

def reverse_str(string: str) -> str:
    return string[::-1]
print(reverse_str('Welcome home!'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""
print('-' * 15)
print('Task 5')

def longest_word(string: list[str]) -> str:
    longest = str('')
    for word in string:
        if len(longest) < len(word):
            longest = word
    return longest

print(longest_word(['hello0', 'worl', 'hellorrrr', 'wor', 'hello', 'world']))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print('-' * 15)
print('Task 6')

def find_substring(str1: str, str2: str):
    str3 = str1.find(str2)
    return str3

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера."""
print('-' * 15)
print('Task 7')

def part_payment(part, month: int):
    """Функція розраховує повну вартість товару при оплаті частинами

    :param part: вказати місячну плату
    :param month: вказати кількість місяців для оплати
    :return: повертає ціну за товар
    """

    return part * month

print(part_payment(1179, 18))

# task 8
"""Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
"""
print('-' * 15)
print('Task 8')

def rem_from_div(number: int, divisor: int) -> int:
    """Функція розраховує і виводить остачу від ділення числа

    :param number: вказати число з якого треба отримати остачу
    :param divisor: вказати число на яке будемо ділити
    """
    remainder = number % divisor
    print(f'Остача від ділення {str(number)} % {str(divisor)} = {str(remainder)} ')

rem_from_div(8019, 8)
rem_from_div(7248, 6)

# task 9
'''
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими'''
print('-' * 15)
print('Task 9')

def str_list(free_list: list) -> list[str]:
    """Функція приймає ліст з будь-якими значеннями і виводить ліст лише зі значеннями типу str

    :param free_list: введіть ліст з довільними значеннями
    :return: повертає ліст із відібраними значеннями типу str
    """
    list_with_str = []
    for i in free_list:
        if type(i) == str:
            list_with_str.append(i)
    return list_with_str

print(str_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

# task 10
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
print('-' * 15)
print('Task 10')

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

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 6, 2]))