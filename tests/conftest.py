import asyncio
import os

import allure
import pytest
import pytest_asyncio
from dotenv import load_dotenv, find_dotenv
from playwright.async_api import async_playwright, expect

from pages.chronos.home_page import HomePage
from pages.chronos.login_page import LoginPage


@pytest_asyncio.fixture()
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(args=['--start-maximized'], headless=False)
        yield browser
        await browser.close()


@pytest_asyncio.fixture
async def page(browser):
    page = await browser.new_page(no_viewport=True, accept_downloads=True)
    yield page
    await page.close()


@pytest.fixture
async def logged_in_browser(page):
    """
    Fixture que realiza el login y retorna un navegador autenticado.
    """
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    url = os.getenv("URL_CHRONOS")
    username = os.getenv("USER_CHRONOS")
    password = os.getenv("PASS_CHRONOS")

    if not url or not username or not password:
        raise ValueError("URL_NEMESIS, USER_NAME, y PASSWORD deben estar configurados en las variables de entorno.")
    login_page = LoginPage(page)
    await login_page.navigate(url)
    await login_page.set_username(username)
    await login_page.set_password(password)
    await login_page.click_on_login_button()
    home_page_ = HomePage(page)
    await expect(home_page_.logout_button).to_be_visible(timeout=80000)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = None

        if "page" in item.funcargs:
            page = item.funcargs["page"]
        elif "logged_in_browser" in item.funcargs:
            page = item.funcargs["logged_in_browser"]

        if page:
            try:
                # Usar el bucle de eventos existente
                loop = asyncio.get_event_loop()
                loop.run_until_complete(take_screenshot(page))
            except Exception as e:
                print(f"Error capturing screenshot: {e}")


async def take_screenshot(page):
    screenshot_binary = await page.screenshot(full_page=True)
    allure.attach(
        screenshot_binary,
        name="screenshot_on_failure",
        attachment_type=allure.attachment_type.PNG
    )
