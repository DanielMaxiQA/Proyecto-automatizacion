from playwright.async_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.locator("//button[@title='Logout']")
        self.toolbar_menu = page.locator("//button[@title='Menu']")
        self.reports_option = page.locator("//mat-panel-title[contains(text(),'Reports')]")
        self.agent_ar_report = page.get_by_role("link", name="Agent A/R")

    async def click_on_toolbar_menu(self) -> None:
        await self.toolbar_menu.click(timeout=5000)

    async def click_on_reports_option(self) -> None:
        await self.reports_option.click(timeout=5000)

    async def click_on_agent_ar_report(self):
        await self.agent_ar_report.click()
