import allure
import pytest
from playwright.async_api import expect

from pages.chronos.agent_ar_page import AgentARPage
from pages.chronos.home_page import HomePage


@allure.feature('Agent Reports Test')
class TestReportAgentAR:

    @allure.story('cualquier cosa')
    @pytest.mark.asyncio
    async def test_report_agent_ar(self, logged_in_browser):
        home_page = HomePage(logged_in_browser)
        with allure.step("Hacemos clic en el toolbar"):
            await home_page.click_on_toolbar_menu()
        with allure.step("Seleccionamos la opcion reportes"):
            await home_page.click_on_reports_option()
        with allure.step("Seleccionados reportes Agent A/R"):
            await home_page.click_on_agent_ar_report()
            agent_ar = AgentARPage(logged_in_browser)
            await agent_ar.set_begin_date("02/10/2025")
            await agent_ar.set_end_date("02/12/2025")
            await agent_ar.click_view_button()
            expect(agent_ar.abrir_en_nueva_pestana_button).to_be_enabled(timeout=80000)
            await agent_ar.click_test()
