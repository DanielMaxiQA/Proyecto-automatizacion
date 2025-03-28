from playwright.async_api import Page


class AgentBalancePage:

    def __init__(self, page: Page):
        self.page = page
        self.reports_option = page.locator("//mat-panel-title[contains(text(),'Reports')]")
        self.agent_balance_report = page.get_by_role("link", name="Agent Balance ")
        self.agent_button = page.locator("//button[@id='btnSearchAgentModal1']")
        self.input_agent_search = page.locator("//input[@name='search']")
        self.input_agent_code = page.locator("text='0020-TX'")
        self.input_begin_date = page.locator("//input[@name='BeginD']")
        self.input_end_date = page.locator("//input[@name='EndD']")
        self.view_button = page.get_by_role("button", name="View")
        self.abrir_en_nueva_pestana_button = page.get_by_role("button", name="Abrir en nueva pestaña")

    async def click_on_reports_option(self) -> None:
        await self.reports_option.click(timeout=5000)

    async def click_on_agent_balance_report(self):
        await self.agent_balance_report.click()

    async def click_agent_button(self):
        await self.agent_button.click()

    async def set_agent_code(self, agent_code: str) -> None:
        await self.input_agent_search.fill(agent_code, timeout=5000)

    async def click_agent_code(self):
        await self.input_agent_code.click()

    async def set_begin_date(self, begin_date: str) -> None:
        await self.input_begin_date.fill(begin_date, timeout=5000)

    async def set_end_date(self, end_date: str) -> None:
        await self.input_end_date.fill(end_date, timeout=2000)

    async def click_view_button(self):
        await self.view_button.click()

    async def click_test(self):
        await self.abrir_en_nueva_pestana_button.click(timeout=80000)