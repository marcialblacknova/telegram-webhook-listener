from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        return "Ignored"
    if "my_chat_member" in data:
        user = data["my_chat_member"]["from"]
        first_name = user.get("first_name", "Usuario")
        message = f"👋 <b>¡Bienvenido, {first_name} a la Red Despierta!</b>\nYa eres parte del círculo privado de <b>BLACKNOVA</b>.\n<i>Comparte con autenticidad ⚡</i>"
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        })
    return "OK"