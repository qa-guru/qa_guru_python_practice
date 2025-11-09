from enum import Enum, auto, IntEnum, StrEnum


class Timeout(int, Enum):
    DEFAULT = auto()
    BIG = auto()
    SMALL = auto()
    MEDIUM = auto()


print(Timeout.MEDIUM.value)
# if 1 is Timeout.DEFAULT.value:
#     print("OK")
# if 2 is Timeout.DEFAULT.value:
#     print("OK")


class Status(str, Enum):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    BLOCKED = 'Blocked'


for item in Status:
    print(item.value)


class HTTP(IntEnum):

    OK = 200
    NOT_FOUND = 404


print(HTTP.OK)
print(HTTP.NOT_FOUND)


class COOKIES(StrEnum):
    TOKEN = "CookieToken"
    LANG = "CookieLang"

print(COOKIES.LANG)
print(COOKIES.TOKEN)

