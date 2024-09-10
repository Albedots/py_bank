from fastapi import FastAPI

from pydantic import BaseModel

import datetime

app = FastAPI()



# ---------------------- TESTE API OK! -------------------------
# @app.get("/")
# def read_root():
#     return {"Minha1": "API"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# -------------------------------------------------------------

#SALDO INICIAL
# SALDO INICIAL
saldo = 500

# Controle de saques diários
saques_dia = 0
data_ultimo_saque = datetime.date.today()

# Limite por saque e limite de saques por dia
VALOR_MAX_SAQUE = 500
LIMITE_SAQUES_DIA = 3

#MODELO DE REQUISIÇÃO
class Transacao(BaseModel):
    amount: float 

@app.post("/deposito")
def deposit(transaction: Transacao):
    global saldo
    if transaction.amount > 0:
        saldo += transaction.amount
    return {"message": "Deposit successful", "saldo": saldo}

@app.post("/saque")
def withdraw(transaction: Transacao):
    global saldo, saques_dia, data_ultimo_saque

    hoje = datetime.date.today()

# Reseta o contador de saques se for um novo dia
    if hoje != data_ultimo_saque:
        saques_dia = 0
        data_ultimo_saque = hoje

    # Verifica se o número máximo de saques foi atingido
    if saques_dia >= LIMITE_SAQUES_DIA:
        return {"message": "Número máximo de saques por dia atingido!", "saldo": saldo}

    # Validações do valor do saque
    if transaction.amount <= 0:
        return {"message": "Valor inválido para saque", "saldo": saldo}
    elif transaction.amount > saldo:
        return {"message": "Saldo insuficiente", "saldo": saldo}
    elif transaction.amount > VALOR_MAX_SAQUE:
        return {"message": f"Valor máximo por saque é R${VALOR_MAX_SAQUE}", "saldo": saldo}

    # Processa o saque
    saldo -= transaction.amount
    saques_dia += 1

    return {"message": "Withdrawal successful", "saldo": round(saldo, 2)}

@app.get("/saldo")
def get_balance():
    return {"saldo": saldo}


#CONSULTA SALDO:
#curl -X GET 'http://127.0.0.1:8000/saldo'

#FAZER DEPOSITO
#curl -X POST 'http://127.0.0.1:8000/deposito' -H 'Content-Type: application/json' -d '{"amount": 100}'

#FAZER SAQUE
#curl -X POST 'http://127.0.0.1:8000/saque' -H 'Content-Type: application/json' -d '{"amount": 50}'


