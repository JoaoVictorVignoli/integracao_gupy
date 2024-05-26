# Realiza a importação de módulos necessários
import os
import json
import requests
from requests.auth import HTTPBasicAuth

# -------->

# Define URL de chamada
url = "http://atendimento.unifique.com.br/api/publica/chamados"

# Declara credenciais de autenticação
from dotenv import load_dotenv
load_dotenv('./.env')

mail = os.getenv('USER_ACELERATO')
token = os.getenv('PASSWORD_ACELERATO')


# -------->

# Define payload de requisições
payload = {
    'descricao': '<p>teste</p>',
    "organizacao":{"organizacaoKey":2,"nome":"HOMOLOGAÇÃO","ativo":True},
    "equipeDeAtendimento":{"equipeKey":3,"nome":"00. Sem Gatilho"},
    "categoria":{"categoriaKey":1668,"descricao":"NOVO COLABORADOR"},
    "especieDeTicketKey" : "3",
    "projeto":{"projetoKey":2},
    "titulo": "Novo Colaborador teste"
}

# Convertendo o corpo da solicitação para JSON
payload_json = json.dumps(payload)

# Define headers
headers = {
'Content-Type': 'application/json'
}

# Realiza a requisição POST com autenticação básica
response = requests.post(url, headers=headers, data=payload_json, auth=HTTPBasicAuth(mail, token))

print(response.text)