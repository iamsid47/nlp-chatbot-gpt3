from flask import Flask, request, jsonify
# from openai import api as openai.api
import openai
import os 
import json
import requests
# from monday import MondayClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# monday = MondayClient(".D-nEAcHDXc7oFUvB0BjoV4ji1TezrpDZmte5QLpr-QQ")

# This is page access token that you get from facebook developer console.
PAGE_ACCESS_TOKEN = str(os.getenv('ACCESS_TOKEN'))

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# This is API key for facebook messenger.
API = "https://graph.facebook.com/v16.0/me/messages?access_token="+PAGE_ACCESS_TOKEN

@app.route("/webhook", methods=['GET', 'POST'])
def fbverify():
    if request.method == 'GET':
        # Facebook webhook verification
        if request.args.get('hub.verify_token') == PAGE_ACCESS_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Invalid verification token'
    else:
        # Handle incoming Facebook messages
        data = request.get_json()
        if data['object'] == 'page':
            for entry in data['entry']:
                for messaging_event in entry['messaging']:
                    if messaging_event.get('message'):
                        sender_id = messaging_event['sender']['id']
                        message_text = messaging_event['message']['text']
                        response_text = generate_response(message_text)
                        send_message(sender_id, response_text)
                        log_lead(sender_id, message_text, response_text)
        return {"msg":'ok'}
    
# Generate response using OpenAI API
def generate_response(message_text):
    prompt = f'User: {message_text}\nBot:'
    response = openai.Completion.create(
        engine='davinci', prompt=prompt, max_tokens=60, n=1, stop=None, temperature=0.5
    )
    return response.choices[0].text.strip()

# Send message to Facebook Messenger
def send_message(sender_id, response_text):
    data = {
        'recipient': {'id': sender_id},
        'message': {'text': response_text}
    }
    headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {PAGE_ACCESS_TOKEN}'}
    response = requests.post('https://graph.facebook.com/v16.0/me/messages', headers=headers, json=data)
    return response.json()

# Log lead data to JSON file
def log_lead(sender_id, message_text, response_text):
    lead_data = {'sender_id': sender_id, 'message': message_text, 'response': response_text}
    with open('lead_log.json', 'a') as f:
        f.write(json.dumps(lead_data))
        f.write('\n')

if __name__ == "__main__":
    app.debug = True
    app.run()
