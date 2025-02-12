from playwright.async_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.locator("//button[@title='Logout']")
        self.toolbar_menu = page.locator("//button[@title='Menu']")
        self.reports_option = page.locator("//mat-panel-title[contains(text(),'Reports')]")
        self.agent_a_r_report = page.get_by_role("link", name="Agent A/R")