from pages.verification_page import VerificationPage
from utils.screenshot_helper import take_screenshot

def test_navigate_section(driver):
    verification_page = VerificationPage(driver)

    # Navegar a la sección de asociados
    verification_page.navigate_to_asociados_section()
    take_screenshot(driver, "Seccion_asociados_cargada")

    #Navegar a la seccion de personas
    verification_page.navigate_to_personas_section()
    take_screenshot(driver, "Seccion_personas_cargada") 

    #Navegar a la seccion de empresas
    verification_page.navigate_to_empresas_section()
    take_screenshot(driver, "Seccion_empresas_cargada") 

    #Navegar a la seccion de beneficios
    verification_page.navigate_to_beneficios_section()  
    take_screenshot(driver, "Seccion_beneficios_cargada")   

    
