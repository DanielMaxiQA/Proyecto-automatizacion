import pytest

from pages.base_page import BasePage


@pytest.mark.asyncio
async def test_navigation(page):
    """Ejemplo de prueba para navegar a una página y verificar el título."""
    base_page = BasePage(page)
    await base_page.navigate_to("https://www.computrabajo.com")
    title = await base_page.get_title()
    assert title == "Example Domain"
