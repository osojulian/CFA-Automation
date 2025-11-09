from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_helper import take_screenshot
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class ContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_contact = (By.LINK_TEXT, "Canales de contacto")
        self.link_pqrs = (By.LINK_TEXT, "PQRS")

        #Campos del formulario
        self.tipo_solicitud = (By.ID, "tipo_solicitud")
        self.nombre_field = (By.NAME, "nombre")
        self.identidad_field = (By.NAME, "documento_identidad")
        self.correo_field = (By.NAME, "email")
        self.telefono_field = (By.NAME, "telefono")
        self.asunto_field = (By.NAME, "asunto")
        self.descripcion_field = (By.NAME, "descripcion")
        self.checkbox_terminos = (By.XPATH, '//label[@class="jet-form-builder__field-label for-checkbox"]')  # Selector para el checkbox


        self.enviar_button = (By.CSS_SELECTOR, 'button.jet-form-builder__action-button.jet-form-builder__submit[type="submit"]')  # Selector para el botón de envío



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


    def open_pqrs_form(self):
        print("Abriendo seccion PQRS")
        wait = WebDriverWait(self.driver, 15)

        # Cerrar el modal si aparece
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

        # Esperar a que aparezca el menú principal
        menu_element = wait.until(EC.presence_of_element_located(self.menu_contact))

                # click en canales de contacto
        menu_element = wait.until(EC.element_to_be_clickable(self.menu_contact))
        menu_element.click()

        # Ahora hacer clic en el enlace PQRS
        pqrs_element = wait.until(EC.element_to_be_clickable(self.link_pqrs))
        pqrs_element.click()

        print("Navegando a la página PQRS...")

                # 7️⃣ Restaurar scroll normal
        self.driver.execute_script("""
            window.onscroll = null;
            document.body.style.overflow = 'auto';
        """)
        time.sleep(2)
    

    def send_pqrs(self, nombre, correo, telefono, asunto, descripcion, identidad):
        print("LLenando formulario PQRS....")

        wait = WebDriverWait(self.driver, 30)

        # Seleccionar tipo de solicitud
        wait.until(EC.presence_of_element_located(self.tipo_solicitud))
        tipo_select = Select(self.driver.find_element(*self.tipo_solicitud))
        tipo_select.select_by_visible_text("Sugerencia") # o "Queja", "Recurso", "Sugerencia". "Peticion"

        self.driver.find_element(*self.nombre_field).send_keys(nombre)
        self.driver.find_element(*self.identidad_field).send_keys(identidad)
        self.driver.find_element(*self.correo_field).send_keys(correo)
        self.driver.find_element(*self.telefono_field).send_keys(telefono)
        self.driver.find_element(*self.asunto_field).send_keys(asunto)
        self.driver.find_element(*self.descripcion_field).send_keys(descripcion)


        # Desplazar la pantalla hacia abajo para que el checkbox sea visible
        self.driver.execute_script("window.scrollBy(0, 500);")  # Ajusta el valor de 500 según sea necesario
        time.sleep(1)  # Esperar un momento para que el desplazamiento se complete

        try:
            ## ALternativa de clic en checkbox y boton enviar con manejo de excepciones
            label = wait.until(EC.element_to_be_clickable(self.checkbox_terminos))
            self.driver.execute_script("arguments[0].scrollIntoView(block: 'center');", label)
            time.sleep(1)  # Esperar un momento para que el desplazamiento se complete
            label.click()
            print("Checkbox de términos seleccionado mediante etiqueta.")

            #Verificar que quedo marcado
            checkbox_input = self.driver.find_element(By.XPATH, '//input[@name="field_name"]')
            if checkbox_input.is_selected():
                print("✓ Verificado: Checkbox marcado correctamente.")
            else:
                print("⚠ Advertencia: Checkbox no marcado, forzando con JavaScript...")
                self.driver.execute_script("arguments[0].checked = true;", checkbox_input)

        except Exception as e:
            print(f"Error al hacer clic en label: {e}")
            # Plan B: JavaScript directo
            checkbox_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="field_name"]')))
            self.driver.execute_script("""
                arguments[0].checked = true;
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, checkbox_input)
            print("✓ Checkbox marcado mediante JavaScript.")

        # Desplazar hacia el botón de envío
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        

                # Asegurarse de que el botón sea clicable
        enviar_button = wait.until(EC.element_to_be_clickable(self.enviar_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", enviar_button)
        try:
            enviar_button.click()
        except ElementClickInterceptedException:
            print("El botón está bloqueado, intentando hacer clic mediante JavaScript.")
            self.driver.execute_script("arguments[0].click();", enviar_button)
        
        
        try:
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[contains(text(), "Gracias") or contains(text(), "recibido")]')
                )
            )
            print("PQRS enviada correctamente.")
            take_screenshot(self.driver, "pqrs_enviada")

        except TimeoutException:
            take_screenshot(self.driver, "error_envio_pqrs")
            print("No se detecto confirmacion de envio")
            assert False, "No se confirmo el envio del formulario PQRS"