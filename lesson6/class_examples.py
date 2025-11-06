class Cat:

    def __init__(self, name, year, color=None):
        self.name = name
        self.year = year
        self.color = color

    def walk(self):
        print(f'Cat "{self.name}" walk ... ')


new_cat = Cat('Черныщ', 2012, 'black')

print(new_cat.name)
print(new_cat.year)

red_cat = Cat('Red', 2010, 'red')

print(red_cat.name)
print(red_cat.year)
print(red_cat.color)
red_cat.walk()


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


a = Vector()
print(a.validate(101))
print(a.norm2(101, 9))


class Token:
    ENCODING = 'utf-8'

    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_valid(value: str):
        return value.isalnum() and value.isascii()

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(data.decode(cls.ENCODING))


raw = 'QWER12345'

print(Token.is_valid(raw))

t1 = Token.from_bytes(b"world")
t2 = Token.from_bytes(b"QWER12345")

print(t1.value)
print(t2.value)


class Alive:
    def __init__(self, year):
        self.year = year

    def alive(self):
        print(f'It is alive ({self.year})')


class Animal:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def speak():
        print('speak')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)


class Cat(Animal, Alive):

    def __init__(self, name, year, color=None):
        super().__init__(name)
        Alive.__init__(self, year)
        self.color = color

    def walk(self):
        print(f'Cat "{self.name}" walk ... ')


animal = Animal('Animal')
animal.speak()

dog = Dog('Bob')
dog.speak()
print(dog.name)

cat = Cat('Черныщ', 2012, 'black')
print(cat.name)
cat.walk()
cat.speak()
cat.alive()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def print_data(self):
        print(f"Пользователь с именем {self.__name} и возрастом {self.__age}")


tom = Person("Tom", 26)
tom.print_data()
tom.__age = 10
tom.__name = '10'
print(tom.__age)
print(tom.__name)
print(tom.age)
print(tom.name)


class Alive:
    def __init__(self, year):
        self.year = year

    def alive(self):
        print(f'It is alive ({self.year})')


class Animal:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def speak():
        print('speak')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        s = f"{self.name.strip()} make Woof"
        print(s)


class Cat(Animal, Alive):

    def __init__(self, name, year, color=None):
        super().__init__(name)
        Alive.__init__(self, year)
        self.color = color

    def walk(self):
        print(f'Cat "{self.name}" walk ... ')

    def speak(self):
        s = f"{self.name.strip()} make Meow"
        print(s)


animal = Animal('Animal')
animal.speak()

dog = Dog('Bob')
dog.speak()
print(dog.name)

cat = Cat('Черныщ', 2012, 'black')
print(cat.name)
cat.walk()
cat.speak()
cat.alive()

