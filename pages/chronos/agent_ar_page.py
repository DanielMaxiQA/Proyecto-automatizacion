from playwright.async_api import Page


class AgentARPage:

    def __init__(self, page: Page):
        self.page = page
        self.input_begin_date = page.locator("//input[@name='BeginD']")
        self.input_end_date = page.locator("//input[@name='EndD']")
        self.view_button = page.get_by_role("button", name="View")
        self.abrir_en_nueva_pestana_button = page.get_by_role("button", name="Abrir en nueva pestaña")
        self.loading = page.get_by_role("img")

    async def set_begin_date(self, begin_date: str) -> None:
        await self.input_begin_date.fill(begin_date, timeout=5000)

    async def set_end_date(self, end_date: str) -> None:
        await self.input_end_date.fill(end_date, timeout=2000)

    async def click_view_button(self):
        await self.view_button.click()

    async def click_test(self):
        await self.abrir_en_nueva_pestana_button.click(timeout=80000)