from pages.login_page import LoginPage


def test_forgot_password_link_present(page):
    login = LoginPage(page)
    login.goto()
    assert login.has_forgot_password_link()=='Forgot password?'
