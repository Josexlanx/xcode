import pyautogui
import time

# Solicita el mensaje y la cantidad de repeticiones
mensaje = input("¿Qué mensaje deseas enviar?: ")
repeticiones = int(input("¿Cuántas veces deseas repetir el mensaje?: "))

# Espera unos segundos antes de empezar a enviar los mensajes

time.sleep(5)

# Enviar el mensaje la cantidad de veces indicada
for _ in range(repeticiones):
    pyautogui.typewrite(mensaje)  # Escribe el mensaje
    pyautogui.press("enter")
    print("Mensaje enviado")      # Envía el mensaje
    time.sleep(0.1)               # Pequeña pausa entre mensajes para evitar posibles bloqueos

print(f"Se envió el mensaje '{mensaje}' {repeticiones} veces.")
input("Presiona Enter para cerrar la consola...")
