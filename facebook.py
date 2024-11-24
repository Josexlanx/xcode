import requests

# URL de autenticación
url = "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzMyMzk4NTI5LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next"

# Datos de autenticación
data = {
    "email": "970253123",  # Usuario o número de teléfono
    "pass": "kittybebe1212"  # Contraseña
}

# Encabezados requeridos
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Referer": "https://www.facebook.com/",
    "Origin": "https://www.facebook.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

# Cookies necesarias
cookies = {
    "ps_l": "1",
    "ps_n": "1",
    "sb": "1UOgZvqwPcCaJ2Dj-F0GSbNB",
    "datr": "1UOgZvcn4Gg3Vkd--rR_sWT0",
    "wd": "825x953",
    "fr": "1XZfNXtw6cnQJXps2.AWU0aAAvsrHmAiUpXwfwO6SyzD4.BnQkFf..AAA.0.0.BnQk3F.AWVzuIx4qxU"
}

# Enviar solicitud POST
response = requests.post(url, data=data, headers=headers, cookies=cookies, allow_redirects=False)

# Analizar respuesta
if response.status_code == 302:
    print("Login successful (redirection detected).")
    print("Cookies:", response.cookies)
else:
    print("Login failed.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
