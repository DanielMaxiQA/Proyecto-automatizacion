import os
import sys
import time
from asyncio import timeout

import allure
import pytest
from playwright.async_api import expect
from pages.chronos.agent_balance_page import AgentBalancePage
from pages.chronos.home_page import HomePage
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from take_screen import take_screenshot


@allure.feature('Agent Reports Test')
class TestReportAgentBalance:

    @allure.story('Reportes Agent-Balance')
    @pytest.mark.asyncio
    async def test_report_agent_balance(self, logged_in_browser, page):
        home_page = HomePage(logged_in_browser)
        agent_balance_page = AgentBalancePage(logged_in_browser)

        with allure.step("Hacer clic en el toolbar"):
            await home_page.click_on_toolbar_menu()
            await take_screenshot(page, "Menú Toolbar")
        with allure.step("Seleccionar la opción reportes"):
            await agent_balance_page.click_on_reports_option()
            await take_screenshot(page, "Menú Reportes")
        with allure.step("Seleccionar reportes Agent Balance"):
            await agent_balance_page.click_on_agent_balance_report()
        with allure.step("Seleccionar agencia"):
            await agent_balance_page.click_agent_button()
            await agent_balance_page.set_agent_code("0020-T")
            await agent_balance_page.click_agent_code()
            await take_screenshot(page, "Reportes Agent Balance")
            await agent_balance_page.set_begin_date("02/10/2025")
            await agent_balance_page.set_end_date("02/12/2025")
            await take_screenshot(page, "Rango de fechas")
            await agent_balance_page.click_view_button()
            await take_screenshot(page, "Obteniendo reporte")
            expect(agent_balance_page.abrir_en_nueva_pestana_button).to_be_enabled(timeout=80000)
            await agent_balance_page.click_test()
            time.sleep(2)
            await take_screenshot(page, "Resultado del reporte")
            time.sleep(5)

