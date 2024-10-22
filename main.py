from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Modelo de Pessoa
class Pessoa(BaseModel):
    nome_completo: str
    data_nascimento: str
    endereco: str
    cpf: str
    estado_civil: str

# Simulando banco de dados na memória
banco_dados: List[Pessoa] = []

# Rotas
@app.post("/pessoas/")
def cadastrar_pessoa(pessoa: Pessoa):
    banco_dados.append(pessoa)
    return pessoa

@app.get("/pessoas/", response_model=List[Pessoa])
def listar_pessoas():
    return banco_dados

@app.get("/pessoas/{cpf}", response_model=Pessoa)
def consultar_pessoa(cpf: str):
    for pessoa in banco_dados:
        if pessoa.cpf == cpf:
            return pessoa
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

@app.put("/pessoas/{cpf}")
def atualizar_pessoa(cpf: str, pessoa_atualizada: Pessoa):
    for i, pessoa in enumerate(banco_dados):
        if pessoa.cpf == cpf:
            banco_dados[i] = pessoa_atualizada
            return pessoa_atualizada
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

@app.delete("/pessoas/{cpf}")
def deletar_pessoa(cpf: str):
    for i, pessoa in enumerate(banco_dados):
        if pessoa.cpf == cpf:
            del banco_dados[i]
            return {"detail": "Pessoa excluída com sucesso"}
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")
