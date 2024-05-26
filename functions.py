import unicodedata
import re
from ldap3 import Server, Connection, SUBTREE, MODIFY_REPLACE
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

load_dotenv(override=True)

# Varaiveis de acesso aos sistemas
server = Server(os.getenv("AD"))
user_ad = os.getenv("USER_AD")
password_ad = os.getenv("PASSWORD_AD")
user_acelerato = os.getenv("USER_ACELERATO")
password_acelerato = os.getenv("PASSWORD_ACELERATO")
url_acelerato = os.getenv("URL_CRIAR_CHAMADO")

def removerAcentosECaracteresEspeciais(palavra):
    """
    A remoção de acentos foi baseada em uma resposta no Stack Overflow.
    http://stackoverflow.com/a/517974/3464573
    """
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def possibilidadesLogonNameAd(nome_canditado):
    nome_canditado = str(nome_canditado).lower()
    lista_excecao = ['de', 'das', 'dos', 'e', 'da']
    possibilidades_logon_name = []
    nomes = str(nome_canditado).split()
    quantidade_nomes = len(nomes)
    for i in range(1 ,quantidade_nomes):
        sobrenome = nomes[-1] if i == 1 else nomes[-i]
        if sobrenome not in lista_excecao:
            logon_name = f"{nomes[0]}.{sobrenome}"
            possibilidades_logon_name.append(logon_name)
    for i in range(1 ,quantidade_nomes):
        sobrenome = nomes[-1] if i == 1 else nomes[-i]
        if sobrenome not in lista_excecao:
            logon_name_abreviado = f"{nomes[0]}.{sobrenome[0]}"
            if logon_name_abreviado not in possibilidades_logon_name:
                possibilidades_logon_name.append(logon_name_abreviado)    
    return possibilidades_logon_name

def pesquisarLogonNameAd(user_names):

    conn = Connection(server, user=user_ad, password=password_ad, )

    if not conn.bind():
        print("Falha na autenticacao")
        exit()

    for user in user_names:
        user_name = f'{user}@redeunifique.com.br'
        conn.search(
            search_base='DC=redeunifique,DC=com,DC=br',  # Substitua pelo seu domínio AD
            search_filter=f'(&(objectClass=user)(userPrincipalName={user_name}))',
            search_scope=SUBTREE,
            attributes=['Name']  # Atributos a serem recuperados
        )
        if len(conn.entries) == 0:
            return user
        
def criarTarefaNovoColaborador():
    
    # nome_colaborador = str(nome_colaborador).upper()

    headers = {
    'Content-Type': 'application/json'
    }


    payload = {
    'descricao': '<p>teste</p>',
    "especieDeTicketKey" : "3",
    "projeto" : {"projetoKey" : 2},
    "titulo": f"NOVO ACESSO: TESTE"
    }

    json_payload = json.dumps(payload)

    response = requests.post(url_acelerato, headers=headers, data=json_payload, auth=HTTPBasicAuth(user_acelerato,user_acelerato))
    print(response.status_code)
    if response.status_code == 200:
        print(f'Tarefa Criada {response.text}')
    else:
        print(f'Erro ao criar tarefa: {response.status_code} | {response.text}')
    

criarTarefaNovoColaborador()