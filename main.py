from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # ✅ Filtrar SOLO cuando un nuevo usuario se une
    if "message" in data and "new_chat_members" in data["message"]:
        chat_id = data["message"]["chat"]["id"]

        for member in data["message"]["new_chat_members"]:
            first_name = member.get("first_name", "BLACKNOVA")
            welcome_message = f"🎉¡Bienvenid@, {first_name} a la Red Despierta!
            Ya eres parte del círculo privado de BLACKNOVA.
            Comparte con auntenticidad.⚡"

            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {"chat_id": chat_id, "text": welcome_message}
            requests.post(url, json=payload)

    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
