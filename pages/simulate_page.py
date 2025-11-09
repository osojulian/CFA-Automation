from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class SimulatePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_simulate = (By.CSS_SELECTOR, 'input.e-search-input[type="search"]')
        self.button = (By.CSS_SELECTOR, 'button.e-search-submit[type="submit"]')
        self.enlace = (By.LINK_TEXT, "simulador")
        self.monto_field = (By.ID, "monto")
        self.simular_button = (By.ID, "plazo")
        self.calcular_button = (By.XPATH, '//button[@class="cfa-button" and text()="Calcular"]')
        self.resultado_simulador = (By.ID, 'resultado')


        

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

    def search(self, term, monto, plazo):
            
            try:

                # Cerrar el modal si aparece
                self.close_modal_if_present()

                print("Realizando búsqueda...")
                wait = WebDriverWait(self.driver, 20) 

                search_field = wait.until(EC.presence_of_element_located(self.menu_simulate))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_field)
                time.sleep(1)  # Esperar un momento para que el desplazamiento se complete

                search_field.clear()
                search_field.send_keys(term)
                print(f"Término de búsqueda ingresado: {term}")
                time.sleep(1)  # Esperar un momento antes de hacer clic en el botón

                ## Hacer enter
                search_field.send_keys(Keys.RETURN) # Presionar Enter para buscar
                print("Búsqueda enviada.")
                
                # Esperar unos segundos para ver el resultado visualmente
                time.sleep(2)

                enlace = wait.until(EC.element_to_be_clickable(self.enlace))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", enlace)
                time.sleep(1)  # Esperar un momento para que el desplazamiento se complete
                enlace.click()
                print("Enlace del simulador clicado.")
                # Esperar que cargue la nueva página
                time.sleep(2)

                self.driver.find_element(*self.monto_field).send_keys(monto)
                self.driver.find_element(*self.simular_button).send_keys(plazo)
                self.driver.find_element(*self.calcular_button).click()

                wait.until(EC.presence_of_element_located(self.resultado_simulador))
                print("Simulación realizada con éxito.")

                # Esperar unos segundos para ver el resultado visualmente
                time.sleep(2)

            except Exception as e:

                print(f"Error durante la búsqueda: {e}")
                return False
            
            



    

            
