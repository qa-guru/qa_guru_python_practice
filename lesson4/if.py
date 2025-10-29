debug_mode = True
if debug_mode:
    pass  # TODO: заглушка

# Обычный if else
x = 10
if x > 0:
    print("Positive")
else:
    print("negative")

# if elif else
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Проверка нескольких условий if elif else
score = 73
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)

# Булева логика
# Любое выражение приводится к True или False.
# «Ложными» считаются: False, None, 0, пустые контейнеры
# ("", [], {}, set()), пустой range(0).
x = 10
if x > 0:
    print("Положительное")

name = input("Имя: ").strip()
if name:  # непустая строка -> True
    print("Привет,", name)

# Вложенные условия
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Вход разрешён")
    else:
        print("Нужен документ")
else:
    print("Сначала исполнится 18")

# Логические операторы
temp = 22
sunny = True
if 18 <= temp <= 28 and sunny:
    print("Идём гулять")

if not False:
    print("False")  # данное условие истинно, поэтому будет напечатано "False"

if True or False:  # оператор "или". Если хотя бы одно из условий истинно, то будет выполнен блок кода
    print("True")

if True and False:  # оператор "и". Если оба условия истинны, то будет выполнен блок кода
    print("something")

# Проверка наличия элемента в структуре
user_list = []
if user_list:
    pass

items_count = 0
if items_count:
    pass

if 'abc':
    pass

# Тернарный (условный) оператор
result = "чётное" if x % 2 == 0 else "нечетное"
print(result)


# match/case
status_code = 404

match status_code:
    case 200:
        print("Успех")
    case 400 | 401 | 403:
        print("Ошибка клиента")
    case 404:
        print("Не найдено")
    case _:
        print("Другое")

# несколько значений в одном case
day = input("Enter a day of the week: ").strip().lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a weekday. Time to work!")
    case "saturday" | "sunday":
        print("It's the weekend. Enjoy your rest!")
    case _:
        print("Unknown day. Please enter a valid weekday name.")

status_code = 404

match status_code:
    case 200:
        print("Успех")
    case 400 | 401 | 403:
        print("Ошибка клиента")
    case 404:
        print("Не найдено")
    case _:
        print("Другое")