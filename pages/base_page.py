from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate_to(self, url: str):
        """Navega a una URL específica."""
        await self.page.goto(url)

    async def get_title(self):
        """Obtiene el título de la página."""
        return await self.page.title()
