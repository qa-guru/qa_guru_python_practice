from dataclasses import dataclass, asdict, replace


class User:
    def __init__(self, name, age, tags=None):
        self.name = name
        self.age = age
        self.tags = tags or []


@dataclass()
class UserDataClass:
    name: str
    age: int
    tags: list[str]

    def __post_init__(self):
        if self.age < 0:
            raise ValueError(" age >= 0 ")


user_dc = UserDataClass('Max', 0, ["a", "c"])
print(user_dc)

user_dc.age = 90
print(user_dc)

user_dc2 = UserDataClass('Max', 90, ["a", "c"])
print(user_dc2)

print(asdict(user_dc2))
print(asdict(user_dc))


user_dc3 = replace(user_dc2, age=31)

print(user_dc3)


print(user_dc == user_dc2)



