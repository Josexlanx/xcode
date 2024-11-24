from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Ruta para manejar el mensaje entrante
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()

    # Pregunta inicial
    if incoming_msg == "hola":
        resp.message("Hola, ¿eres empleado de Aercaribe? Responde con 'Sí' o 'No'.")
    
    # Respuesta en caso de "Sí"
    elif incoming_msg == "sí":
        resp.message("Gracias por confirmar. ¿Te gustaría recibir noticias y actualizaciones? (Responde con 'Sí' o 'No')")
    
    # Respuesta en caso de "No"
    elif incoming_msg == "no":
        resp.message("Gracias. Si tienes alguna otra pregunta, no dudes en escribir.")
    
    # Respuesta para cualquier otra entrada
    else:
        resp.message("Por favor, responde solo con 'Sí' o 'No' para continuar.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
