class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[id="sdo-login"]')
        self.password_input = page.locator('input[id="sdo-password"]')
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('div[role="alert"] >> text=Bad credentials.')
        self.forgot_password_link = page.locator("button.auth-link")

    def goto(self):
        self.page.goto("https://dev2.getinfo.radugi.net/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error(self):
        return self.error_message.inner_text()

    def has_forgot_password_link(self):
        return self.forgot_password_link.inner_text()
