from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.company_page import CompanyPage
from data import users
import pytest

def test_access_company_page(page):
    login = LoginPage(page)
    login.goto()
    login.login(users.valid_user['username'], users.valid_user['password'])

    dashboard = DashboardPage(page)
    dashboard.goto_company()

    assert "company" in page.url

@pytest.mark.xfail(reason="not equals")
def test_director_matches_current_user(page):
    login = LoginPage(page)
    login.goto()
    login.login(users.valid_user['username'], users.valid_user['password'])

    dashboard = DashboardPage(page)
    dashboard.goto_company()

    company = CompanyPage(page)
    assert company.get_director() == company.get_current_user()
