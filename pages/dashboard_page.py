class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.company_link = page.locator('a[href] >> text=Company')
        self.educational_center=page.locator('span[data-cy="submenu-title-ms-education-center"]')

    def goto_company(self):
        self.educational_center.click()
        self.company_link.is_visible()
        self.company_link.click()
        self.page.wait_for_url("**/company/**")
