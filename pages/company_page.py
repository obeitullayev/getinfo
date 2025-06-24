class CompanyPage:
    def __init__(self, page):
        self.page = page
        self.director_name = page.locator("div.description", has_text="Head").locator("a")
        self.profile = page.locator('header span.el-avatar')
        self.current_user= page.locator('div.font-bold.text-center')

    def get_director(self):
        return self.director_name.inner_text()

    def get_current_user(self):
        self.profile.click()
        return self.current_user.inner_text()
