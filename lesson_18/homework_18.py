import logging
logging.basicConfig(force=True,
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

print('Ітератор 1')
def rev_it(nu: list):
    reverse_iter = iter(nu[::-1])
    for i in reverse_iter:
        print(i)

rev_it(list(range(10)))

print('-'*15)
print('Ітератор 2')

def even_it(n: int):
    numbers = iter(list(range(n+1)))
    for i in numbers:
        if i % 2 == 0:
            print(i)

even_it(14)

print('-'*15)
print('Генератор 1')

def even_gen(n: int):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for i in even_gen(9):
    print(i)

print('-'*15)
print('Генератор 2')

def fib_gen(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a = b
        b = a + b

for i in fib_gen(9):
    print(i)

print('-'*15)
print('Декоратор 1')

def decor_log(func):
    def wrapper(*args):
        logging.info(f'Ім\'я функції - {func.__name__}')
        result = func(*args)
        logging.info(f'Аргументи функції {args}')
        logging.info(f'Результат функції {result}')
        return result
    return wrapper

@decor_log
def multiply(num1, num2):
    return num1 * num2

multiply(3, 6)
multiply(2, 4)

print('-'*15)
print('Декоратор 2')

def decor_exeption(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            logging.info(e)

    return wrapper

@decor_exeption
def div(num1, num2):
    return num1 / num2

div(5, 'e')
div(5, 0)
