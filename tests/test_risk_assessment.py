import time

import allure
import pytest
from playwright.async_api import expect

from pages.home_page import HomePage
from pages.risk_assessment_page import RiskAssessmentPage
from resources.data.nemesis_data import RISK_ASSESSMENT_DATA


@allure.feature('Risk Assessment')
class TestRiskAssessment:

    @allure.story('Testing Risk Assessment')
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_home_page_functionality(self, logged_in_browser, setup_download_directory):
           with allure.step("Se inicia sesion en Nemesis "):
                  home_page = HomePage(logged_in_browser)
           with allure.step("Se valida que estemos en el Home de Nemesis"):
                  await expect(home_page.toolbar_menu_options).to_be_visible(timeout=8000)
           with allure.step("Se ingresa a Risk Assessment"):
                  await home_page.click_option_menu_risk_assessment()
                  await home_page.click_risk_assessment()
           risk_assessment_page = RiskAssessmentPage(logged_in_browser)
           with allure.step("Se configura los parametros de busqueda"):
                  await risk_assessment_page.select_month_(RISK_ASSESSMENT_DATA["month"])
                  await risk_assessment_page.select_year_(RISK_ASSESSMENT_DATA["year"])
                  await risk_assessment_page.click_search_button(0)
                  await risk_assessment_page.select_state_(RISK_ASSESSMENT_DATA["state"])
                  await risk_assessment_page.click_search_button(1)
                  await risk_assessment_page.select_register_table(5)
           with allure.step("Se descarga el archivo y se valida su descarga"):
                  download_dir = setup_download_directory
                  file_path = risk_assessment_page.download_file(download_dir)
                  assert await risk_assessment_page.verify_file_downloaded(await file_path)
           time.sleep(5)