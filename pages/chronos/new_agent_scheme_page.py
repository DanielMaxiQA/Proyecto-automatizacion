import time
from asyncio import timeout

from playwright.async_api import Page, expect


class AgentSchemePage:

    def __init__(self, page: Page):
        self.page = page
        self.button_agent_option = page.get_by_role("button", name="Agents")
        self.button_agent_scheme = page.get_by_role("link", name="Agent-Scheme", exact=True)
        self.text_search_agent = page.get_by_role("heading", name="Search Agent")
        self.input_search_agent = page.locator("#AgentSearchBar")
        self.button_open_search_agent = page.locator("#btnSearchAgentModal")
        self.option_agent_select = page.locator("//div[contains(text(),'18067')]")
        self.button_add_scheme = page.get_by_role("button", name="Add ")
        self.checkbox_is_enabled = page.get_by_text("Is Enabled:")
        self.combo_country_currency = page.get_by_role("combobox")
        self.option_co_us = "4"
        self.input_nickname = page.locator("form").filter(has_text="Country/Currency: ARGENTINA-").get_by_role("textbox").first
        self.input_description = page.locator("form").filter(has_text="Country/Currency: ARGENTINA-").get_by_role("textbox").nth(1)
        self.button_fee = page.locator("#btnSearchFeeModal")
        self.input_fee_name = page.get_by_label("Fee Name :")
        self.option_fee_list = page.get_by_role("cell", name="10/T 1/K", exact=True)
        self.button_commission = page.locator("#btnSearchCommissionModal")
        self.input_commission_name = page.locator("#CommissionsSearchBar")
        self.option_commission_name = page.get_by_role("cell", name="% $100 60%")
        self.input_spread = page.get_by_role("row", name="    Select All").get_by_role("textbox").nth(3)
        self.button_save = page.get_by_role("button", name="Save")
        self.button_confirm_save = page.get_by_role("button", name="  Yes")
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

    async def click_on_add_agent_scheme(self) -> None:
        await self.button_add_scheme.click(timeout=3000)

    async def click_on_check_is_enabled(self) -> None:
        await self.checkbox_is_enabled.click(timeout=2000)

    async def click_on_country_currency(self) -> None:
        await self.combo_country_currency.click(timeout=2000)

    async def click_on_option_co_us(self) -> None:
        await self.combo_country_currency.select_option(self.option_co_us)

    async def set_input_nickname(self, nickname: str) -> None:
        await  self.input_nickname.fill(nickname, timeout=2000)

    async def set_input_description(self, description: str) -> None:
        await  self.input_description.fill(description, timeout=2000)

    async def click_on_button_fee(self) -> None:
        await self.button_fee.click(timeout=2000)

    async def set_input_fee_name(self, fee_name) -> None:
        await self.input_fee_name.fill(fee_name, timeout=2000)

    async def click_on_option_fee_list(self) -> None:
        await self.option_fee_list.click(timeout=2000)

    async def click_on_button_commission(self) -> None:
        await self.button_commission.click(timeout=2000)

    async def set_input_commission(self, commission_percentage: str) -> None:
        await self.input_commission_name.fill(commission_percentage, timeout=2000)

    async def click_on_option_commission(self) -> None:
        await self.option_commission_name.click(timeout=2000)

    async def set_input_spread(self, spread: str) -> None:
        await self.input_spread.type(spread, delay=200)
        await self.page.wait_for_timeout(1000)
        await self.page.keyboard.press("Enter")

    async def click_on_button_save(self) -> None:
        await self.button_save.click(timeout=5000)

    async def click_on_button_confirm_save(self) -> None:
        await self.button_confirm_save.click(timeout=3000)

    async def click_on_button_close(self) -> None:
        await self.button_close.click(timeout=3000)





