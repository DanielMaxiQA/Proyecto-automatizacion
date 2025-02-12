from playwright.async_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.input_username = page.locator('#username')
        self.input_password = page.locator('#password')
        self.button_login = page.locator("#kc-login")

    async def navigate(self, url: str) -> None:
        await self.page.goto(url, timeout=100000, wait_until="networkidle")

    async def set_username(self, username: str) -> None:
        await self.input_username.fill(username, timeout=20000)

    async def set_password(self, password: str) -> None:
        await self.input_password.fill(password)

    async def click_on_login_button(self) -> None:
        await self.button_login.click()
