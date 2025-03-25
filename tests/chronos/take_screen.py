import allure
from playwright.async_api import Page


class TakeScreen:

    def __init__(self, page: Page):
        self.page = page


async def take_screenshot(page, step_name):
    screenshot = await page.screenshot(full_page=True)
    allure.attach(
        screenshot,
        name=f"{step_name}.png",
        attachment_type=allure.attachment_type.PNG
    )