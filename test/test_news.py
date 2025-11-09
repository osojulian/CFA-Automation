from pages.news_page import NewsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_open_news_section(driver):
    news_page = NewsPage(driver)
    news_page.open_news_section()


    # Verifico que la URL sea la correcta
    current_url = driver.current_url.lower()
    assert "cfa.com.co/noticias" in current_url, \
        f"La URL actual no corresponde a Noticias CFA: {current_url}"

    # Esperar que el título sea visible (maneja delays o animaciones)
    wait = WebDriverWait(driver, 20)
    titulo = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//h2[contains(translate(., "NOTICIASCFA", "noticiascfa"), "noticias cfa")]')
    )
    )

    assert titulo.is_displayed(), "El título 'Noticias CFA' no está visible en la página."
    print("✅ Validación de Noticias CFA completada con éxito.")