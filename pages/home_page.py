from playwright.async_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page= Page
        self.toolbar_menu_options = page.locator("//ul[@data-bind='foreach: MenuOptions']")
        self.option_menu_risk_assessment = page.locator(
            "//a[@class ='dropdown-toggle' and contains(text(), 'Risk Assessment')]")
        self.risk_assessment = page.locator("//a[contains(text(),'Risk Assessment Dashboard')]")

    async def is_displayed_toolbar_menu(self) -> bool:
        await expect(self.toolbar_menu_options).to_be_visible(timeout=8000)
        return await self.toolbar_menu_options.is_visible()

    async def click_option_menu_risk_assessment(self) -> None:
        await self.option_menu_risk_assessment.click()

    async def click_risk_assessment(self) -> None:
        await self.risk_assessment.click()
