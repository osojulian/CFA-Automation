import pytest
from pages.login_page import LoginPage
from utils.screenshot_helper import take_screenshot


def test_login_exitoso(driver):
    login = LoginPage(driver)

    #Defino credenciales
    user = "1033342645"
    password = "4567"
    login.login(user, password)
    take_screenshot(driver, "flujo_completado")

    #valido que se detecte el teclado virtual
    page_source = driver.page_source
    assert "Ingrese su clave personal" in page_source, "No se cargo el teclado virtual correctamente"


