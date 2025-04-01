import os
import sys
import time
import allure
import pytest
from playwright.async_api import expect

from pages.chronos.delete_agent_scheme_page import DeleteAgentSchemePage
from pages.chronos.home_page import HomePage
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from take_screen import take_screenshot

@allure.feature('Agent Scheme')
class TestAgentScheme:
    @allure.story('New Agent Scheme')
    @pytest.mark.asyncio

    async def test_edit_agent_scheme(self, logged_in_browser, page):
        home_page = HomePage(logged_in_browser)
        delete_agent_scheme_page = DeleteAgentSchemePage(logged_in_browser)

        with allure.step("Hacer clic en el toolbar"):
            await home_page.click_on_toolbar_menu()
            await take_screenshot(page, "Menú Toolbar")
        with allure.step("Hacer clic en el Menú Agent"):
            await delete_agent_scheme_page.click_on_agent_option()
            await take_screenshot(page, "Menú Agent")
        with allure.step("Hacer clic en el Menú Agent Scheme"):
            await delete_agent_scheme_page.click_on_agent_scheme()
            time.sleep(2)
            expect(delete_agent_scheme_page.text_search_agent).to_be_enabled(timeout=80000)
            await take_screenshot(page, "Búsqueda de agencia")
        with allure.step("Buscar Agencia"):
            await delete_agent_scheme_page.set_search_agent("18067")
            time.sleep(4)
            expect(delete_agent_scheme_page.option_agent_select).to_be_visible(timeout=80000)
            #time.sleep(2)
            await delete_agent_scheme_page.click_on_agent_select()
            await take_screenshot(page, "Agencia Seleccionada")
        with allure.step("Eliminar un Esquema"):
            await delete_agent_scheme_page.click_on_element_scheme()
            time.sleep(5)
            await delete_agent_scheme_page.click_on_button_delete()
            time.sleep(4)
            await take_screenshot(page, "Confirmar eliminar esquema seleccionado")
            await delete_agent_scheme_page.click_on_button_confirm_save()
            await page.wait_for_timeout(6000)
            time.sleep(1)
            await take_screenshot(page, "Schema Eliminado Correctamente")
            await delete_agent_scheme_page.click_on_button_close()
            time.sleep(5)




