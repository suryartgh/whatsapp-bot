from flask import Flask, jsonify, request
import requests  # You need to import requests

app = Flask(__name__)

# WhatsApp API credentials
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your WhatsApp Business API token
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"  # Replace with your WhatsApp Business API phone number ID

# Predefined message
PREDEFINED_MESSAGE = "Welcome! I can help you with movie details. Reply with the name of a movie, and I'll assist you."

@app.route('/')
def home():
    return jsonify({"message": "WhatsApp Bot is Running!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Check if a message was received
    if 'messages' in data:
        message = data['messages'][0]
        sender = message['from']
        text = message['text']['body'].lower()

        # Check the content of the user's message
        if text == "hii":
            send_whatsapp_message(sender, PREDEFINED_MESSAGE)

    return "OK", 200

def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v16.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message},
    }
    requests.post(url, json=payload, headers=headers)

if __name__ == '__main__':
    print("Starting WhatsApp Bot...")
    app.run(port=5000, debug=True)
