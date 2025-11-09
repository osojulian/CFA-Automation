from pages.simulate_page import SimulatePage
from utils.screenshot_helper import take_screenshot

def test_simulate_search(driver):
    simulate_page = SimulatePage(driver)

    # Defino el término de búsqueda
    search_term = "Simulador de credito"
    monto = "50000000"
    plazo = "12"

    # Realizo la búsqueda
    simulate_page.search(search_term, monto, plazo)

    # Tomo una captura de pantalla
    take_screenshot(driver, "Simulador_búsqueda_realizada")