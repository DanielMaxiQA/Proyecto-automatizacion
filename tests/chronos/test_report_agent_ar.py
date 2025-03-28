import os
import sys
import time
from asyncio import timeout

import allure
import pytest
from playwright.async_api import expect
from pages.chronos.agent_ar_page import AgentARPage
from pages.chronos.home_page import HomePage
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from take_screen import take_screenshot


@allure.feature('Agent Reports Test')
class TestReportAgentAR:

    @allure.story('Reportes Agent-AR')
    @pytest.mark.asyncio
    async def test_report_agent_ar(self, logged_in_browser, page):
        home_page = HomePage(logged_in_browser)
        agent_ar_page = AgentARPage(logged_in_browser)

        with allure.step("Hacer clic en el toolbar"):
            await home_page.click_on_toolbar_menu()
            await take_screenshot(page, "Menú Toolbar")
        with allure.step("Seleccionar la opción reportes"):
            await agent_ar_page.click_on_reports_option()
            await take_screenshot(page, "Menú Reportes")
        with allure.step("Seleccionar reportes Agent A/R"):
            await agent_ar_page.click_on_agent_ar_report()
            await agent_ar_page.set_begin_date("02/10/2025")
            await agent_ar_page.set_end_date("02/12/2025")
            await take_screenshot(page, "Rango de fechas")
            await agent_ar_page.click_view_button()
            time.sleep(2)
            await take_screenshot(page, "Obteniendo reporte")
            expect(agent_ar_page.open_in_new_window_button).to_be_enabled(timeout=100000)
            await take_screenshot(page, "Resultado del reporte")
            time.sleep(4)
            await agent_ar_page.click_new_window()
            time.sleep(5)

