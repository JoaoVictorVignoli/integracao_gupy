# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions import removerAcentosECaracteresEspeciais, possibilidadesLogonNameAd, pesquisarLogonNameAd, criarTarefaNovoColaborador

app = FastAPI()

class WebhookPayload(BaseModel):
    companyName: str
    id: str
    event: str
    date: str
    data: dict

@app.post("/webhook")
async def receive_webhook(payload: WebhookPayload):
    companyName = payload.companyName
    id = payload.id
    date = payload.date
    event = payload.event
    data = payload.data

    dados_vaga = data
    
    nome_candidato = f"{dados_vaga['candidate']['name']} {dados_vaga['candidate']['lastName']}"
    nome_candidato_sem_acentos = removerAcentosECaracteresEspeciais(nome_candidato)
    logon_name_ad = possibilidadesLogonNameAd(nome_candidato_sem_acentos)
    resultado_pesquisa_ad = pesquisarLogonNameAd(logon_name_ad)

    print(criarTarefaNovoColaborador(nome_candidato, resultado_pesquisa_ad))
    
    if event == "candidate.hired":
        return {"message": "Novo Colaborador contratado"}
 
    # Se nenhum caso correspondente for encontrado, você pode retornar uma resposta padrão
    return {"message": "Webhook received successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

