from playwright.async_api import Page


class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.input_username = page.locator('#loginName')
        self.input_password = page.locator('#password')
        self.button_login = page.locator("//button[contains(text(),'Login')]")
        self.label_error_login = page.locator("//li[contains(text(),'You may have mistyped your username or password, p')]")


    async def navigate(self, url: str)-> None:
        await self.page.goto(url)

    async def set_username(self, username: str)-> None:
        await self.input_username.fill(username)

    async def set_password(self, password: str)-> None:
        await self.input_password.fill(password)

    async def click_on_login_button(self)-> None:
        await self.button_login.click()

    async def is_displayed_label_error_login(self) -> bool:
        return await self.label_error_login.is_visible()