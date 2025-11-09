from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
import time
from selenium.common.exceptions import TimeoutException


class VerificationPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_asociados = (By.LINK_TEXT, "Asociados")
        self.menu_personas = (By.LINK_TEXT, "Personas")
        self.menu_empresas = (By.LINK_TEXT, "Empresas")
        self.menu_beneficios = (By.LINK_TEXT, "Beneficios")



    def close_modal_if_present(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            modal_btn = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.dialog-close-button.dialog-lightbox-close-button")
            ))
            # Esperar un momento para que termine la animación de entrada
            time.sleep(0.5)

                # Forzar clic JS
            self.driver.execute_script("arguments[0].click();", modal_btn)
            print("Modal cerrado correctamente (JS click).")

                # Esperar que desaparezca del DOM
            wait.until_not(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a.dialog-close-button.dialog-lightbox-close-button")
            ))

            # Bloquear scroll temporalmente después de cerrar
            self.driver.execute_script("document.body.style.overflow = 'hidden';")
            print("🔒 Scroll bloqueado temporalmente.")
            time.sleep(0.5)


        except TimeoutException:
            print("✅ No se encontró modal (continuando normalmente).")
        except Exception as e:
            print(f"Error al intentar cerrar modal: {e}")


    def navigate_to_asociados_section(self):

        wait = WebDriverWait(self.driver, 10)
        # Cerrar el modal si está presente
        self.close_modal_if_present()

        # Navegar al menú de asociados
        asociados_menu = wait.until(EC.element_to_be_clickable(self.menu_asociados))
        asociados_menu.click()
        asociados_menu.click()  # Segundo clic para asegurar la navegación
        print("Navegado al menú de asociados.")

        wait = WebDriverWait(self.driver, 10)
        # Esperar a que la sección de asociados se cargue
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div[1]/div/div[1]/div[1]/h1[contains(text(), "¡Asóciate a cfa y mejora tu calidad de vida!")]')
            )
        )

        ##Tomo captura de pantalla
        take_screenshot(self.driver, "Carga_seccion_asociados")
        print("Pantalla de carga de sección de asociados capturada.")

        # Esperar unos segundos para ver el resultado visualmente
        time.sleep(2)

    def navigate_to_personas_section(self):
        wait = WebDriverWait(self.driver, 10)
        # Cerrar el modal si está presente
        self.close_modal_if_present()

        # Navegar al menú de personas
        personas_menu = wait.until(EC.element_to_be_clickable(self.menu_personas))
        personas_menu.click()
        personas_menu.click()  # Segundo clic para asegurar la navegación
        print("Navegado al menú de personas.")

        wait = WebDriverWait(self.driver, 10)
        # Esperar a que la sección de personas se cargue
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//p[contains(text(), "Opciones de ahorro, crédito y soluciones")]')
            )
        )

        ##Tomo captura de pantalla
        take_screenshot(self.driver, "Carga_seccion_personas")
        print("Pantalla de carga de sección de personas capturada.")

        # Esperar unos segundos para ver el resultado visualmente
        time.sleep(2)

    def navigate_to_empresas_section(self):
        wait = WebDriverWait(self.driver, 10)
        # Cerrar el modal si está presente
        self.close_modal_if_present()

        # Navegar al menú de empresas
        empresas_menu = wait.until(EC.element_to_be_clickable((self.menu_empresas)))
        empresas_menu.click()
        empresas_menu.click()  # Segundo clic para asegurar la navegación
        print("Navegado al menú de empresas.")

        wait = WebDriverWait(self.driver, 10)
        # Esperar a que la sección de empresas se cargue
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//p[contains(text(), "Impulsa el crecimiento de tu empresa")]')
            )
        )

        ##Tomo captura de pantalla
        take_screenshot(self.driver, "Carga_seccion_empresas")
        print("Pantalla de carga de sección de empresas capturada.")

        # Esperar unos segundos para ver el resultado visualmente
        time.sleep(2)

    def navigate_to_beneficios_section(self):
        wait = WebDriverWait(self.driver, 10)
        # Cerrar el modal si está presente
        self.close_modal_if_present()

        # Navegar al menú de beneficios
        beneficios_menu = wait.until(EC.element_to_be_clickable((self.menu_beneficios)))
        beneficios_menu.click()
        beneficios_menu.click()  # Segundo clic para asegurar la navegación
        print("Navegado al menú de beneficios.")

        wait = WebDriverWait(self.driver, 10)
        # Esperar a que la sección de beneficios se cargue
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h1[contains(text(), "Accede a los beneficios")]')
            )
        )

        ##Tomo captura de pantalla
        take_screenshot(self.driver, "Carga_seccion_beneficios")
        print("Pantalla de carga de sección de beneficios capturada.")

        # Esperar unos segundos para ver el resultado visualmente
        time.sleep(2)