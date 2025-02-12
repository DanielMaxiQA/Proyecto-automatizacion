import os

import allure
import pytest
from dotenv import find_dotenv, load_dotenv
from playwright.async_api import expect

from pages.chronos.home_page import HomePage
from pages.chronos.login_page import LoginPage


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


@allure.feature('Login Chronos')
class TestLoginChronos:

    @allure.story('Usuario puede iniciar sesión en Chronos')
    @pytest.mark.smoke
    @pytest.mark.asyncio
    async def test_login(self, page):
        login_page = LoginPage(page)
        with allure.step("Se abre la aplicacion"):
            await login_page.navigate(os.getenv("URL_CHRONOS"))
        with allure.step("Se ingresa los datos de inicio de sesion"):
            await login_page.set_username(os.getenv("USER_CHRONOS"))
            await login_page.set_password(os.getenv("PASS_CHRONOS"))
            await login_page.click_on_login_button()
        with allure.step("Se valida que estamos logueados"):
            home_page = HomePage(page)
            await expect(home_page.logout_button).to_be_visible(timeout=20000)

