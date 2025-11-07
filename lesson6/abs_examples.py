from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Browser(Protocol):
    def goto(self, url: str) -> None: ...

    def click(self, locator: tuple[str, str]) -> None: ...

    def text(self, locator: tuple[str, str]) -> str: ...


class SeleniumBrowser:
    def goto(self, url): ...

    def click(self, locator): ...

    def text(self, locator): return "Welcome"


class PlaywrightBrowser:
    def goto(self, url): ...

    def click(self, locator): ...

    def text(self, locator): return "Welcome"


def open_home(b: Browser) -> str:
    b.goto("/home")
    return b.text(("css", "h1"))


sb = SeleniumBrowser()
pb = PlaywrightBrowser()
print(open_home(sb), open_home(pb))  # обе реализации подходят


assert isinstance(sb, Browser)  # True благодаря @runtime_checkable


# === Абстракция браузера (ABC с NotImplementedError по умолчанию) ===
class Browser(ABC):
    def goto(self, url: str) -> None:
        raise NotImplementedError("Browser.goto() is not implemented")

    def click(self, locator: tuple[str, str]) -> None:
        raise NotImplementedError("Browser.click() is not implemented")

    def fill(self, locator: tuple[str, str], text: str) -> None:
        raise NotImplementedError("Browser.fill() is not implemented")

    def text(self, locator: tuple[str, str]) -> str:
        raise NotImplementedError("Browser.text() is not implemented")

    def wait_visible(self, locator: tuple[str, str], timeout: float = 5.0) -> None:
        raise NotImplementedError("Browser.wait_visible() is not implemented")


# === Абстрактная страница (ABC) ===
class Page(ABC):
    URL: str

    def __init__(self, browser: Browser):
        self.b = browser

    @abstractmethod
    def open(self) -> "Page": ...

    @abstractmethod
    def is_loaded(self) -> bool: ...


# === Конкретная страница: Главная ===
class HomePage(Page):
    URL = "/home"
    H1 = ("css", "h1.title")
    LOGIN = ("css", "a.login")

    def open(self) -> "HomePage":
        self.b.goto(self.URL)
        self.b.wait_visible(self.H1)
        return self

    def is_loaded(self) -> bool:
        return bool(self.b.text(self.H1))  # тут дернётся Browser.text()

    def go_to_login(self) -> "LoginPage":
        self.b.click(self.LOGIN)
        return LoginPage(self.b)


class LoginPage(Page):
    URL = "/login"
    USER = ("id", "username")
    PASS = ("id", "password")
    SUBMIT = ("css", "button[type=submit]")
    BANNER = ("css", ".banner")

    def open(self) -> "LoginPage":
        self.b.goto(self.URL)
        self.b.wait_visible(self.USER)
        return self

    def is_loaded(self) -> bool:
        return bool(self.b.text(self.BANNER))

    def login_as(self, username: str, password: str) -> HomePage:
        self.b.fill(self.USER, username)
        self.b.fill(self.PASS, password)
        self.b.click(self.SUBMIT)
        return HomePage(self.b)


# === Частично реализованный “браузер” — специально НЕ реализует .text() ===
class FakeBrowser(Browser):
    def __init__(self):
        self.url = ""
        self.dom: dict[tuple[str, str], str] = {}

    def goto(self, url: str) -> None:
        self.url = url
        if url == "/home":
            self.dom = {
                ("css", "h1.title"): "Welcome!",
                ("css", "a.login"): "Log in",
            }
        elif url == "/login":
            self.dom = {
                ("css", ".banner"): "Please sign in",
                ("id", "username"): "",
                ("id", "password"): "",
                ("css", "button[type=submit]"): "Sign in",
            }
        else:
            self.dom = {}

    def click(self, locator: tuple[str, str]) -> None:
        if self.url == "/home" and locator == ("css", "a.login"):
            self.goto("/login")
        elif self.url == "/login" and locator == ("css", "button[type=submit]"):
            self.goto("/home")

    def fill(self, locator: tuple[str, str], text: str) -> None:
        self.dom[locator] = text

    def wait_visible(self, locator: tuple[str, str], timeout: float = 5.0) -> None:
        pass



def test_flow(browser: Browser):
    home = HomePage(browser).open()
    assert home.is_loaded()  # ← здесь произойдёт NotImplementedError
    login = home.go_to_login()
    assert login.is_loaded()
    home2 = login.login_as("elena", "secret")
    assert home2.is_loaded()


fake = FakeBrowser()
try:
    test_flow(fake)
except NotImplementedError as e:
    print("Ожидаемая ошибка:", e)


from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Browser(ABC):

    @abstractmethod
    def goto(self, url):
        raise NotImplementedError("Browser.goto() -> Not Implemented")

    @abstractmethod
    def click(self, element):
        raise NotImplementedError("Browser.click() -> Not Implemented")

    @abstractmethod
    def fill(self, element):
        raise NotImplementedError("Browser.fill() -> Not Implemented")

class FireFox(Browser):
    NAME = 'FireFox'

    def goto(self, url):
        print(f'{self.NAME} - GOTO: {url}')

    def click(self, element):
        print(f'{self.NAME} - CLICK: {element}')

    def fill(self, element):
        print(f'{self.NAME} - FILL: {element}')


class Chrome(Browser):
    NAME = 'Chrome'

    def goto(self, url):
        print(f'{self.NAME} - GOTO: {url}')

    def click(self, element):
        print(f'{self.NAME} - CLICK: {element}')

    def fill(self, element):
        print(f'{self.NAME} - FILL: {element}')


class Page(ABC):
    URL: str

    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def open(self): ...

class HomePage(Page):
    URL = '/home'
    H1 = ('css', 'h1')
    DIV = ('css', 'DIV')

    def open(self):
        self.browser.goto(self.URL)

    def click_on_div(self):
        self.browser.click(self.H1)


class LoginPage(Page):
    URL = '/login'
    INPUT_PASS = ('css', 'input1')
    INPUT_LOGIN = ('css', 'input2')
    BUTTON_SUBMIT = ('css', 'submit')

    def open(self):
        self.browser.goto(self.URL)

    def login(self):
        self.browser.goto(self.URL)
        self.browser.fill(self.INPUT_LOGIN)
        self.browser.fill(self.INPUT_PASS)
        self.browser.click(self.BUTTON_SUBMIT)



ff = FireFox()
home = HomePage(ff)

home.open()
home.click_on_div()


chrome = Chrome()
home = HomePage(chrome)

home.open()
home.click_on_div()


login = LoginPage(ff)
login.open()
login.login()


login = LoginPage(chrome)
login.open()
login.login()



