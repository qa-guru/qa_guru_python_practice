for n in [10, 20, 30]:
    pass

# Перебор списка
nums = [10, 20, 30]
for n in nums:
    print(n)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Перебор символов строки
for ch in "hi":
    print(ch)

# Перебор диапазона чисел: start, stop (не включительно), step
for i in range(1, 6, 2):  # 1, 3, 5
    print(i)

# Использование range()
for i in range(10):
    print(i)  # 0..9

for i in range(1, 11):
    print(i)  # 1..10

for i in range(1, 11, 2):
    print(i)  # 1, 3, 5, 7, 9

nums = [10, 20, 30]

# Простой проход
for n in nums:
    print(n)

# Индекс + значение
for i, n in enumerate(nums):  # i: 0.., n: элемент
    print(i, n)

# Фильтрация на лету
for n in nums:
    if n % 20 == 0:
        print("divisible by 20:", n)

s = "QA"
for ch in s:
    print(ch)

# С индексом
for i, ch in enumerate(s):
    print(i, ch)

point = (10, 20)
for coord in point:
    print(coord)

# Распаковка в цикле
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, ch in pairs:
    print(num, ch)

# Проход по дикту
user = {"name": "Elena", "age": 29, "skills": ["Python", "QA"]}

# По ключам (по умолчанию — то же самое, что for k in user:)
for k in user.keys():
    print(k)

# По значениям
for v in user.values():
    print(v)

# По парам ключ-значение
for k, v in user.items():
    print(k, "=>", v)

# Итерируем вложенные структуры
stack = {
    "alice": {"role": "QA", "level": "senior"},
    "bob": {"role": "BE", "level": "middle"},
}
for name, info in stack.items():
    print(name, ":", info["role"], info["level"])

courses = {
    "python": ["loops", "dicts", "tests"],
    "qa": ["test design", "playwright"],
}
for course, topics in courses.items():
    for t in topics:
        print(course, ":", t)

people = [
    {"name": "Ann", "age": 25},
    {"name": "Bob", "age": 31},
]
for p in people:
    print(p["name"], p["age"])

# Вложенные циклы
for i in range(2):  # range - это функция, которая возвращает последовательность чисел
    for j in range(3):
        print(i,
              j)  # будет напечатано 6 пар чисел, потому что внутренний цикл будет выполнен 3 раза для каждой итерации внешнего цикла

# генераторы списков
#  [<выражение> for <переменная> in <итерируемое> if <условие>]
# квадраты чисел 0..4
squares = [x*x for x in range(5)]            # [0, 1, 4, 9, 16]

# только чётные
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# трансформация строк
upper = [name.strip().upper() for name in ["  elena ", "qa "]]  # ['ELENA', 'QA']


labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']


# Генераторные выражения
total = sum(x*x for x in range(10))

