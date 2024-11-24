import os
import codecs

palabra_elegida = input('Palabra clave: ')
ruta = input('Ruta para leer: ')
contenido = os.listdir(ruta)
found = False

with open("results.txt", "w", encoding='utf-8') as output_file:
    for archivo in contenido:
        if archivo.endswith(".txt"):
            file_path = os.path.join(ruta, archivo)
            with codecs.open(file_path, mode='r', encoding='utf-8', errors='replace') as prueba:
                inside_block = False
                login_pass = ""

                for linea in prueba:
                    if linea.startswith("http://") or linea.startswith("https://") or linea.startswith("android://"):
                        inside_block = palabra_elegida.lower() in linea.lower()
                        if inside_block:
                            parts = linea.strip().split(':', 3)  # Dividir en URL, login, pass (omitiendo el https:// o http://)
                            if len(parts) >= 4:
                                login_pass = f"{parts[2]}:{parts[3]}"
                                print(login_pass)
                                found = True
                                output_file.write(f"{login_pass}\n")
                        continue

    if not found:
        print("No se encontró el enlace solicitado.")
        output_file.write("No se encontró el enlace solicitado.\n")
