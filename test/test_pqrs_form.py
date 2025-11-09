from pages.contact_page import ContactPage
from utils.screenshot_helper import take_screenshot


def test_form_pqrs(driver):
    pqrs = ContactPage(driver)

    #Abrir formulario
    pqrs.open_pqrs_form()
    

    #Llenar datos y enviar
    pqrs.send_pqrs(
        nombre="Julian Osorio",
        identidad="1033342645",
        correo="julian.osorio@test.com",
        telefono="3100000000",
        asunto="Prueba automatizada PQRS",
        descripcion="Esta es una prueba automatizada del formulario PQRS.",
    )

    take_screenshot(driver, "Flujo_pqrs_completado")