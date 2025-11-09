from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
from selenium.common.exceptions import TimeoutException
import time


class NewsPage:
    def __init__(self,driver):
        self.driver = driver
        ## Enlace a asociados
        self.link_asociados = (By.LINK_TEXT, "Asociados")
        self.link_news = (By.LINK_TEXT, "Blog")


        

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

    def open_news_section(self):
        wait = WebDriverWait(self.driver, 10)

        print("Navegando a la sección de Noticias...")


        self.close_modal_if_present()

        print("Esperando a que el menú se estabilice...")

            # 2️⃣ Cancelar cualquier scroll automático o focus script
        self.driver.execute_script("""
            window.scrollTo(0, 0);
            document.body.style.overflow = 'hidden';
            window.onscroll = function() { window.scrollTo(0, 0); };
            document.addEventListener('scroll', e => { window.scrollTo(0, 0); }, true);
        """)

            # 3️⃣ Esperar que la página esté arriba
        time.sleep(1)
        current_scroll = self.driver.execute_script("return window.scrollY;")
        if current_scroll != 0:
            self.driver.execute_script("window.scrollTo(0, 0);")
        print("Scroll bloqueado y reposicionado en la parte superior.")


        #Esperar a que aparezca el menú principal
        menu_element = wait.until(EC.presence_of_element_located(self.link_asociados))

        #Hacer clic en el enlace de asociados
        menu_element.click()
        print("Clic en el enlace de Asociados realizado.")

        # Esperar a que aparezca el enlace de noticias y hacer clic
        news_element = wait.until(EC.element_to_be_clickable(self.link_news))
        news_element.click()
        print("Clic en el enlace de Noticias realizado.")
        print("Navegando a la página de Noticias...")


        ## Esperar a que cargue la página de noticias
        wait.until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "Noticias")]')))
        print("Página de Noticias cargada correctamente.")

        take_screenshot(self.driver, "noticias_visibles")
