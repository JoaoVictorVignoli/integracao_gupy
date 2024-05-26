import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

url_postback = os.getenv('POSTBACK_URL_GUPY')
token = os.getenv('TOKEN_GUPY')

def envia_config():
    url = "https://api.gupy.io/api/v1/webhooks"

    payload = {
        "action": "candidate.hired",
        "postbackUrl": url_postback
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

def verificar_webhooks():

    url = "https://api.gupy.io/api/v1/webhooks?perPage=10&page=1"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print(response.text)

def delete_webhook():

    url = "https://api.gupy.io/api/v1/webhooks/e90a727b-e731-476c-ba89-31ffd3465053"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer a28cea8f-e190-415e-a9a2-f9e20c4b01f0"
    }

    response = requests.delete(url, headers=headers)
    print(response.status_code)


verificar_webhooks()