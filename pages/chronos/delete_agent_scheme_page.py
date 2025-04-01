import time
from asyncio import timeout
from datetime import datetime
from playwright.async_api import Page, expect


class DeleteAgentSchemePage:

    def __init__(self, page: Page):
        self.page = page
        self.button_agent_option = page.get_by_role("button", name="Agents")
        self.button_agent_scheme = page.get_by_role("link", name="Agent-Scheme", exact=True)
        self.text_search_agent = page.get_by_role("heading", name="Search Agent")
        self.input_search_agent = page.locator("#AgentSearchBar")
        self.button_open_search_agent = page.locator("#btnSearchAgentModal")
        self.option_agent_select = page.locator("//div[contains(text(),'18067')]")
        current_date = datetime.today().strftime("%Y-%m-%d")
        date_today = f"Sanity-{current_date}"
        self.element_scheme = page.get_by_text(date_today)
        self.button_delete = page.locator("//button[contains(text(),'Delete')]")
        self.button_confirm_delete = page.get_by_role("button", name="  Yes")
        self.button_close = page.get_by_role("button", name="  Close")


    async def click_on_agent_option(self) -> None:
        await self.button_agent_option.click(timeout=2000)

    async def click_on_agent_scheme(self) -> None:
        await self.button_agent_scheme.click(timeout=5000)

    async def set_search_agent(self, agent_code: str) -> None:
        if await self.input_search_agent.is_visible(timeout=2000):
            await self.input_search_agent.click(timeout=2000)
        else:
            await self.button_open_search_agent.click(timeout=3000)
            time.sleep(2)
        await self.input_search_agent.type(agent_code, delay=300)

    async def click_on_agent_select(self) -> None:
        await self.option_agent_select.click(timeout=2000)

    async def click_on_element_scheme(self) -> None:
        await self.element_scheme.click(timeout=3000)

    async def click_on_button_delete(self) -> None:
        await self.button_delete.click(timeout=3000)

    async def click_on_button_confirm_save(self) -> None:
        await self.button_confirm_delete.click(timeout=3000)

    async def click_on_button_close(self) -> None:
        await self.button_close.click(timeout=3000)





