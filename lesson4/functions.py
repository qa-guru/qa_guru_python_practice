# def имя_функции(параметры):
#     # тело функции (с отступом)
#     # инструции

# Пустая функция (заглушка)
def empty_function():
    pass


# Вызов функции
def greet():
    print("Привет!")


greet()  # выведет: Привет!


# Функция с возвращаемым значением
def say_hello_world(name: str):
    text = f'Hello {name.capitalize()}!'
    return text


text = say_hello_world('alex')
print(text)

text = say_hello_world('oleg')
print(text)


def square(number):
    return number * number


result = square(1)
print(result)

result = square(2)
print(result)

result = square(3)
print(result)

for i in range(6):
    print(square(i))


# Параметры функции
def add(a, b):
    print(f"Summ = {a + b}")


add(5, 3)


def repeat(text, times, separator):
    return f"{text + separator}" * times


print(repeat('Hello', 10, '\t'))


# Позиционные (обязательные) аргументы
def print_name(first, last):
    print('First name: ', first)
    print('Last name: ', last)


print_name('John', 'Doe')


def print_name(first, last, year):
    print('First name: ', first)
    print('Last name: ', last)
    print('Year: ', year)


print_name('John', 'Doe', '2024')
print_name(first='Doe', last='John', year='2024')  # Именованные (keyword) аргументы
print_name('Doe', 'John', year='2024')


# Аргументы по умолчанию (default)
def describe_dog(pet_name, animal_type='dog'):
    print(f'I have a {animal_type} with name {pet_name}')


describe_dog('River')
describe_dog('River', 'cat')
describe_dog('River', animal_type='cat')


# Функция format_text переводит текст в верхний регистр если upper = True

def format_text(text, upper=True):
    if upper:
        return text.upper()
    return text


print(format_text('hello', upper=False))
print(format_text('hello'))

# Реализовать функцию show_work_schedule,
# которая выводит в консоль расписание работы на заданное количество дней, начиная с сегодня.
# В будни выводятся часы работы, в выходные — Closed.
import calendar
from datetime import timedelta


def show_work_schedule(days=7, work_time="9:00-18:00", closed=[5, 6]):
    today = datetime.now()

    for i in range(days):
        day = today + timedelta(days=i)
        weekday = day.weekday()
        day_name = calendar.day_name[weekday]
        status = 'Closed' if weekday in closed else work_time
        print(f"{day_name}: {status}")


show_work_schedule()
show_work_schedule(days=10, closed=[])


# Только позиционные аргументы (positional-only)
# red и blue — строго позиционные
# Можно потребовать, чтобы некоторые параметры можно было передавать только позиционно
def mix_colors(red, blue, /):
    print("Mix:", red, blue)


# Только именованные аргументы (keyword-only)
# name и age — строго именованные
def create_profile(*, name, age):
    print(f"Profile - Name: {name}, Age: {age}")


# Произвольное число аргументов
# Пример (*args)
def mean(*num):
    return sum(num)


print(mean(1, 2, 3, 4, 5, 5, 6, 6, 7, 0))
print(mean(1))
print(mean())

print(mean(0, 9))


def func(*args, **kwargs):
    pass


# Произвольное число аргументов
# Пример (*kwargs)
# Формирует URL с параметрами запроса.
# https://example.com/search?q=python&limit=10
def build_url(base_url, **kwargs):
    if not kwargs:
        return base_url

    query = '&'.join(f"{key}={value}" for key, value in kwargs.items())
    return f"{base_url}?{query}"


url = build_url('https://example.com/search', q='python', limit='10', page='9')
print(url)

url = build_url('https://example.com/search')
print(url)

# Создать универсальную функцию log(),
# которая принимает различные типы аргументов и выводит информацию о событиях в консоль в структурированном виде.
# <level> <event> <args> <meta>
from datetime import datetime

# Комбинированный пример
def log(event, /, *args, level='INFO', **meta):
    print(f'{level}:', event, args, meta)


log('start')
log('download', 'file.txt', 'CRITICAL', user='admin', time=datetime.now().date())
log('download', 'file.txt', user='admin', time=datetime.now().date())

# Рекурсивные функции
# 1 × 2 × 3 × 4 × 5 = 5! = 120
def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def fib(n):
    if n in (0, 1):
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(8))

# Область видимости переменных
x = 'global'


def outer():
    x = 'enclosing'
    y = 'global y '
    global y

    def inner():
        print('def inner', x)

    inner()

    print('def outer', x)


outer()
print('x', x)
print('y', y)

x = 'original global'


def modify():
    global x
    x = 'modified global'


print(x)
modify()
print(x)
