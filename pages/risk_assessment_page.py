import asyncio
import os

from playwright.async_api import Page, expect


class RiskAssessmentPage:

    def __init__(self, page: Page):
        self.page = page
        self.select_month = page.locator("//select[contains(@data-bind,'options: Months')]")
        self.select_year = page.locator("//select[contains(@data-bind,'options: Years')]")
        self.button_search = page.locator("//button[@title='Buscar']")
        self.select_states = page.locator("//select[contains(@data-bind,'options: States')]")
        self.button_export_selected = page.locator("//button[@data-bind='click: ExportExcel']")
        self.checkbox_locator = "//tr/td/div/input[@type='checkbox']"

    async def select_month_(self, month: str) -> None:
        """Selects a specified month from a dropdown or selection interface."""
        try:
            await expect(self.select_month).to_be_visible(timeout=8000)
            await self.select_month.select_option(month)
        except Exception as e:
            raise ValueError(f"Failed to select month '{month}': {e}")

    async def select_year_(self, year: str) -> None:
        """Selects a specified year from a dropdown or selection interface."""
        try:
            await expect(self.select_year).to_be_visible(timeout=8000)
            await self.select_year.select_option(year)
        except Exception as e:
            raise ValueError(f"Failed to select year '{year}': {e}")

    async def click_search_button(self, index: int = 0):
        """Hace clic en el botón de búsqueda dado su índice."""
        await self.button_search.nth(index).click()

    async def select_state_(self, state: str) -> None:
        """Selects a specified state from a dropdown or selection interface."""
        try:
            await expect(self.select_states).to_be_visible(timeout=30000)
            await self.select_states.select_option(state)
        except Exception as e:
            raise ValueError(f"Failed to select state '{state}': {e}")

    async def select_register_table(self, count: int):
        """
        Selecciona una cantidad específica de checkboxes en una tabla.

        Args:
            count (int): Número de checkboxes a seleccionar.

        Raises:
            ValueError: Si no hay suficientes checkboxes disponibles.
        """
        # Localizar todos los checkboxes en la tabla
        elements = self.page.locator(self.checkbox_locator)

        # Validar que haya suficientes elementos
        total_checkboxes = await elements.count()
        if total_checkboxes < 1:
            raise ValueError("No hay checkboxes disponibles en la tabla.")
        if count > total_checkboxes:
            raise ValueError(f"Se solicitaron {count} checkboxes, pero solo hay {total_checkboxes} disponibles.")
        # Seleccionar los primeros `count` checkboxes
        for i in range(count):
            await elements.nth(i).check()

    async def download_file(self, download_dir: str) -> str:
        """
        Hace clic en el botón de descarga y devuelve la ruta completa del archivo descargado.

        Args:
            download_dir (str): Directorio donde guardar el archivo descargado.

        Returns:
            str: Ruta completa del archivo descargado.
        """
        # Capturar el evento de descarga
        async with self.page.expect_download() as download_info:
            await self.button_export_selected.click()

        # Obtener información de la descarga
        download = await download_info.value
        file_name = download.suggested_filename
        final_path = os.path.join(download_dir, file_name)

        print("El archivo descargado es: ", file_name)

        # Guardar el archivo descargado en el directorio especificado
        await download.save_as(final_path)

        return final_path

    async def verify_file_downloaded(self, file_path: str) -> bool:
        """
        Verifica si el archivo existe y no está vacío.

        Args:
            file_path (str): Ruta completa del archivo descargado.

        Returns:
            bool: True si el archivo existe y no está vacío, False de lo contrario.
        """
        return await asyncio.to_thread(os.path.exists, file_path) and await asyncio.to_thread(os.path.getsize,
                                                                                                  file_path) > 0