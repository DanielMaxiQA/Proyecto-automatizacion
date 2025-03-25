import os
import allure
import pytest
from dotenv import find_dotenv, load_dotenv
from playwright.async_api import expect
from pages.chronos.home_page import HomePage
from pages.chronos.login_page import LoginPage
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from take_screen import take_screenshot


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


@allure.feature('Login Chronos')
class TestLoginChronos:

    @allure.story('Usuario puede iniciar sesión en Chronos')
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_login(self, page):
        login_page = LoginPage(page)
        with allure.step("Se abre la aplicación"):
            await login_page.navigate(os.getenv("URL_CHRONOS"))
            await take_screenshot(page, "Abrir Chronos")
        with allure.step("Ingresar los datos de inicio de sesion"):
            await login_page.set_username(os.getenv("USER_CHRONOS"))
            await login_page.set_password(os.getenv("PASS_CHRONOS"))
            await take_screenshot(page, "Credenciales")
            await login_page.click_on_login_button()
        with allure.step("Validar Login Correcto"):
            home_page = HomePage(page)
            await expect(home_page.logout_button).to_be_visible(timeout=20000)
            await take_screenshot(page, "Ingreso a HomePage")
        with allure.step("Hacer clic en toolbar"):
            await home_page.click_on_toolbar_menu()
            await take_screenshot(page, "Menú Toolbar")


