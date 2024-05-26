import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

url = "https://prod-141.westus.logic.azure.com:443/workflows/2e0dad0eb19f402cae93e29556167db9/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=42uPoZsaWORn1mHXDfWdPGbzhKpnVch0b-ruQehae_A"

user_acelerato = os.getenv("USER_ACELERATO")
password_acelerato = os.getenv("PASSWORD_ACELERATO")
url_acelerato = os.getenv("URL_ACELERATO")

def ler_json(arquivo):
    with open(arquivo, 'r') as json_file:
        dados = json.load(json_file)
    return dados

def enviar_webhook_teste(url, data):
    response = requests.post(url, json=data)
    print(response.status_code ,response.text)

dados_novo_colaborador = 'novo_colaborador_teste.json'
novo_colaborador = ler_json(dados_novo_colaborador)
enviar_webhook_teste(url, novo_colaborador)
