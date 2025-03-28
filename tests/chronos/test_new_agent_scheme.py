import os
import sys
from datetime import datetime
import time
from asyncio import timeout
import allure
import pytest
from playwright.async_api import expect

from pages.chronos.new_agent_scheme_page import AgentSchemePage
from pages.chronos.home_page import HomePage
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from take_screen import take_screenshot

@allure.feature('Agent Scheme')
class TestAgentScheme:
    @allure.story('New Agent Scheme')
    @pytest.mark.asyncio

    async def test_agent_scheme(self, logged_in_browser, page):
        home_page = HomePage(logged_in_browser)
        agent_scheme_page = AgentSchemePage(logged_in_browser)

        with allure.step("Hacer clic en el toolbar"):
            await home_page.click_on_toolbar_menu()
            await take_screenshot(page, "Menú Toolbar")
        with allure.step("Hacer clic en el Menú Agent"):
            await agent_scheme_page.click_on_agent_option()
            await take_screenshot(page, "Menú Agent")
        with allure.step("Hacer clic en el Menú Agent Scheme"):
            await agent_scheme_page.click_on_agent_scheme()
            time.sleep(2)
            expect(agent_scheme_page.text_search_agent).to_be_enabled(timeout=80000)
            await take_screenshot(page, "Búsqueda de agencia")
        with allure.step("Buscar Agencia"):
            await agent_scheme_page.set_search_agent("18067")
            time.sleep(2)
            expect(agent_scheme_page.option_agent_select).to_be_visible(timeout=80000)
            #time.sleep(2)
            await agent_scheme_page.click_on_agent_select()
            await take_screenshot(page, "Agencia Seleccionada")
        with allure.step("Nuevo Esquema"):
            await agent_scheme_page.click_on_add_agent_scheme()
            #await page.wait_for_timeout(1000)
            await agent_scheme_page.click_on_check_is_enabled()
            await agent_scheme_page.click_on_country_currency()
            await agent_scheme_page.click_on_option_co_us()
            current_date = datetime.today().strftime("%Y-%m-%d")
            nickname = f"Sanity-{current_date}"
            await agent_scheme_page.set_input_nickname(nickname)
            await agent_scheme_page.set_input_description(nickname)
            await agent_scheme_page.click_on_button_fee()
            await agent_scheme_page.set_input_fee_name("10/T 1/K")
            await page.wait_for_timeout(2000)
            await agent_scheme_page.click_on_option_fee_list()
            await agent_scheme_page.click_on_button_commission()
            await agent_scheme_page.set_input_commission("35%")
            await page.wait_for_timeout(2000)
            await agent_scheme_page.click_on_option_commission()
            await agent_scheme_page.set_input_spread("0.20")
            time.sleep(2)
            await take_screenshot(page, "Datos del nuevo esquema")
            time.sleep(2)
            await agent_scheme_page.click_on_button_save()
            time.sleep(2)
            await agent_scheme_page.click_on_button_confirm_save()
            await page.wait_for_timeout(6000)
            time.sleep(1)
            await take_screenshot(page, "Schema creado Correctamente")
            await agent_scheme_page.click_on_button_close()
            time.sleep(5)




