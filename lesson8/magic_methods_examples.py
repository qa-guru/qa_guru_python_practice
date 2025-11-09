class User:
    def __init__(self, name, age, tags=None):
        self.name = name
        self.age = age
        self.tags = tags or []

    def __eq__(self, name):
        if isinstance(name, str):
            return self.name == name
        else:
            return False

    def __add__(self, num):
        return User(self.name, self.age+num, self.tags)

    def __repr__(self):
        return f"User {self.name}: age = {self.age} with tags = {self.tags}"

user = User('Max', 10, ["a" , "c"])
print(user)

print(user + 1)

print(user == 'Max')