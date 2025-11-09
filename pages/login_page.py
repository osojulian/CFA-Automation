from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.office_field = (By.LINK_TEXT, "Ingreso Oficina Virtual")
        self.user_field = (By.ID, "inp_Documento")
        self.login_button = (By.ID, "btn_continuar")

        self.user_field = (By.ID, "inp_Documento")
        self.login_button = (By.ID, "btn_continuar")


    def login(self, user, password):
        self.driver.find_element(*self.office_field).click()
        # Espera que se abra la nueva pestaña
        self.driver.implicitly_wait(3)

        # Cambia el foco a la nueva ventana
        self.driver.switch_to.window(self.driver.window_handles[-1])


        self.driver.find_element(*self.user_field).send_keys(user)
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.login_button).click()

        wait = WebDriverWait(self.driver, 10)

        print("Esperando carga del teclado virtual...")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="tituloSeccion" and contains(text(), "Ingrese su clave personal")]')
            )
        )

        ##Tomo captura de pantalla
        take_screenshot(self.driver, "teclado_virtual_cargado")
        print("Pantalla de autenticación cargada correctamente (teclado virtual visible).")

    
        time.sleep(2)




        