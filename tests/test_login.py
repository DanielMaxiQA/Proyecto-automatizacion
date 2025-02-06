import os

import allure
import pytest
from dotenv import find_dotenv, load_dotenv
from playwright.async_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


@allure.feature('Login Nemesis')
class TestLogin:

    @allure.story('Usuario puede iniciar sesión con credenciales válidas')
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_login_valid_credentials(self, page):
        login_page = LoginPage(page)
        with allure.step("Abrir aplicacion: "):
            await login_page.navigate(os.getenv("URL_NEMESIS"))
        with allure.step("Se ingresa los datos de inicio de sesion"):
            await login_page.set_username(os.getenv("USER_NAME"))
            await login_page.set_password(os.getenv("PASSWORD"))
            await login_page.click_on_login_button()
        with allure.step("Se valida que estamos logueados"):
            home_page = HomePage(page)
            await expect(home_page.toolbar_menu_options).to_be_visible(timeout=8000)

    @allure.story('Usuario intenta iniciar sesion con credenciales erroneas')
    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_fail(self, page):
        login_page = LoginPage(page)
        await login_page.navigate(os.getenv("URL_NEMESIS"))
        await login_page.set_username("user")
        await login_page.set_password("invalid")
        await login_page.click_on_login_button()
        await expect(login_page.label_error_login).to_be_visible(timeout=8000)
        #assert login_page.is_displayed_label_error_login, "Error message is not displayed"

    @allure.story('Caso de prueba fallido a proposito')
    @pytest.mark.regression
    @pytest.mark.asyncio
    async def test_fail_testing(self, page):
        login_page = LoginPage(page)
        with allure.step("Se abre la aplicacion"):
            await login_page.navigate(os.getenv("URL_NEMESIS"))
        with allure.step("Se ingresa los datos de inicio de sesion"):
            await login_page.set_username("user")
            await login_page.set_password("invalid")
            await login_page.click_on_login_button()
        with allure.step("Se valida que se muestre el label de credenciales incorrectas"):
            await expect(login_page.label_error_login).not_to_be_visible(timeout=8000)
            #assert not login_page.is_displayed_label_error_login, "Error message is not displayed"
