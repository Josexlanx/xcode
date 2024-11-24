import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# URL de autenticación de Joinnus
url = "https://www.joinnus.com/auth/login/async-api"

# Usar MultipartEncoder para manejar multipart/form-data correctamente
data = MultipartEncoder(
    fields={
        "email": "adrian_0_24@hotmail.com",
        "password": "Adrian_0",
        "captcha": "5495827866"
    }
)

# Encabezados y cookies
headers = {
    "Content-Type": data.content_type,  # Esto se genera automáticamente con MultipartEncoder
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "es-US,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "Origin": "https://www.joinnus.com",
    "Referer": "https://www.joinnus.com/auth/login?continue=https%3A%2F%2Fwww.joinnus.com%2F",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# Cookies necesarias en el encabezado
cookies = {
    "_cc_id": "bcab09e5257be2fd811201b0fff821ad",
    "lang": "es",
    "_hjSessionUser_3545751": "eyJpZCI6IjFiMjYwNGQyLWJkYzYtNWJhZi1iOWNjLWViN2ZkODBjMDNlYSIsImNyZWF0ZWQiOjE3Mjk2MTQwNDU2NTgsImV4aXN0aW5nIjp0cnVlfQ==",
    "sendCookies": "1",
    "_clck": "awiuxp%7C2%7Cfqb%7C0%7C1756",
    "ai_user": "yJXTPn8OFEI3cxaExxl6j+|2024-10-25T15:49:38.263Z",
    "consentCookies": "[{\"title\":\"Necesario\",\"key\":\"cookie_necesarias\",\"description\":\"Las cookies necesarias ayudan a hacer una página web utilizable activando funciones básicas como la navegación en la página y el acceso a áreas seguras de la página web. La página web no puede funcionar adecuadamente sin estas cookies.\",\"items\":[\"next-i18next\",\"joinnus2\",\"_ga\",\"consentCookies\"],\"isChecked\":true,\"isMandatory\":true,\"disabled\":true},{\"title\":\"Estadisticas\",\"key\":\"cookie_administration\",\"description\":\"Las cookies estadísticas ayudan a los propietarios de páginas web a comprender cómo interactúan los visitantes con las páginas web reuniendo y proporcionando información de forma anónima.\",\"items\":[\"_ga\"],\"isChecked\":true,\"isMandatory\":false,\"disabled\":false},{\"title\":\"No clasificados\",\"key\":\"cookie_otros\",\"description\":\"Las cookies no clasificadas son cookies para las que todavía estamos en proceso de clasificar, junto con los proveedores de cookies individuales.\",\"items\":[\"next-i18next\"],\"isChecked\":true,\"isMandatory\":false,\"disabled\":false}]",
    "_hjSessionUser_3553215": "eyJpZCI6ImVhOTNiZmE4LTc5NjctNTcyZi05MDI1LTAyYWY5YWU4MTNjOSIsImNyZWF0ZWQiOjE3Mjk4NzI3OTA0NDcsImV4aXN0aW5nIjp0cnVlfQ==",
    "city": "lima",
    "__gads": "ID=2de2bf5e3a07ff5e:T=1729614063:RT=1729894691:S=ALNI_MboACOHexjrgB9-8tKa3KhMOM_T_Q",
    "__gpi": "UID=00000a6268273df8:T=1729614063:RT=1729894691:S=ALNI_MbhmmNcHAsCttDRz5d8nnzaPQkVMA",
    "__eoi": "ID=27885042afa380cf:T=1729614063:RT=1729894691:S=AA-AfjYWzjdQtogftsksESaTTuUX",
    "_ga": "GA1.1.183816436.1729614044",
    "_ga_7CVBBBNPBN": "GS1.2.1729894689.6.1.1729894900.60.0.0",
    "cto_bundle": "FYr60181OGRyaTNrbEVBckI1T1NiNFlmaXZqOEIlMkJCOUczaU1CR1VLTWRVJTJCd3pheklMbzdWVml4alZFd09NeFVhWEFHYXhlNFh1MjB5N1pDMzFTZzdZdjFjSllrVXNmWEM3MXRFb0RWb3ZtbzFaWmRZcWIlMkYwViUyRnFqTU10MSUyQnNORHFBMENSc0dKOWtBa3N0ZXpUTEZZaUhIeXMwV0hIMlJpUTNYa1NLRUpxJTJCJTJGQU84JTJCOE9rSnUlMkIlMkZna3c3Y2hmSWdOcFkyNHZMd1NzayUyQnhIQzd2Qlo4RlY2VXljSFJQb0NCVGRiNUdFUmZua2tnRmNEdllyZ3B4cDFjZkUlMkY5WFdmNXpJJTJGYXo",
    "_ga_6PD7X628CJ": "GS1.1.1729894689.8.1.1729894935.24.0.142840327",
    "joinnus2": "08f1de3e549b16b0478b78c5d795ec31",
    "ai_session": "JMMWNT9zaT3vU8wO60JzG2|1730238574106|1730238574106",
    "next-i18next": "es"
}

# Realizar la solicitud POST con datos y cookies
response = requests.post(url, data=data, headers=headers, cookies=cookies)

# Mostrar respuesta
if response.status_code == 200:
    print("Login successful!")
    print("Response JSON:", response.json())
else:
    print("Login failed.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
