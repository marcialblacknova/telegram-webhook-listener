from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        first_name = message['from']['first_name']
        
        # Mensaje de bienvenida personalizado
        welcome_message = f"¡Bienvenid@, {first_name}! 🌟 Gracias por unirte."
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": welcome_message}
        requests.post(url, json=payload)

    return 'ok', 200

if __name__ == '__main__':
    # Esto mantiene vivo el servidor para Render
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
