# Цикл while
count = 3
while count > 0:
    print(count)
    count -= 1

# Бесконечные циклы
while True > 0:
    print(count)
    count -= 1

# Обратный отсчёт
n = 5
while n > 0:
    print(n)
    n -= 1
print("Старт!")

# Чтение до «стоп-слова»
while True:
    s = input("> ")
    if s == "quit":
        break
    print("Вы ввели:", s)

value = None
while value is None:
    s = input("Введите целое: ")
    if s.lstrip("-").isdigit():
        value = int(s)

# Управление потоком в циклах
for n in range(10):
    if n == 5:
        break  # выйдем из цикла на 5
    if n % 2 == 0:
        continue  # пропустим чётные
    print(n)

n = 10
while n > 0:
    if n == 3:
        break  # принудительный выход — else НЕ выполнится
    n -= 1
else:
    print("Цикл завершился без break")

nums = [2, 4, 6, 9, 12]

# Управление потоком в циклах для цикла for
for n in nums:
    if n % 2 == 1:
        print("found odd:", n)
        break
else:
    print("no odd numbers")


for row in range(1, 3):
    for col in range(1, 4):
        print(row, col)

# Вложенные циклы
row = 1
while row <= 3:
    col = 1
    while col <= 3:
        print(row, col, end="  ")
        col += 1
    print()
    row += 1

# Блок else у циклов
for n in range(3):
    print(n)
else:
    print("Готово")  # выполнится, если не было break

# Пример с break
for n in range(3):
    if n == 1:
        break
else:
    print("Не видим это")  # не выполнится

