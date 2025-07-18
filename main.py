from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # 👉 Detectar si es un join request (cuando el admin aprueba)
    if "chat_join_request" in data:
        join_data = data["chat_join_request"]
        chat_id = join_data["chat"]["id"]
        user = join_data["from"]
        first_name = user.get("first_name", "BLACKNOVA")

        welcome_message = (
            f"🎉 *¡Bienvenido, {first_name} a la Red Despierta!*\n\n"
            "Ya eres parte del círculo privado de *BLACKNOVA*.\n"
            "_Comparte con autenticidad._ ⚡️"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": welcome_message,
            "parse_mode": "MarkdownV2"
        }

        requests.post(url, json=payload)

    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
