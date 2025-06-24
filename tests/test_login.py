from pages.login_page import LoginPage
from data import users


def test_login_error_on_invalid_credentials(page):
    login = LoginPage(page)
    login.goto()
    login.login(users.invalid_user['username'], users.invalid_user['password'])
    assert "Bad credentials." in login.get_error()


def test_successful_login(page):
    login = LoginPage(page)
    login.goto()
    login.login(users.valid_user['username'], users.valid_user['password'])
    assert page.url.startswith("https://dev2.getinfo.radugi.net/")
