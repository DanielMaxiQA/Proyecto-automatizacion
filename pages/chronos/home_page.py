from playwright.async_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.locator("//button[@title='Logout']")
        self.toolbar_menu = page.locator("//button[@title='Menu']")

    async def click_on_toolbar_menu(self) -> None:
        await self.toolbar_menu.click(timeout=5000)


