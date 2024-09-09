from fastapi import FastAPI

from pydantic import BaseModel

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
saldo = 500
#MODELO DE REQUISIÇÃO
class Transacao(BaseModel):
    amount: float

@app.post("/deposito")
def deposit(transaction: Transacao):
    global saldo
    saldo += transaction.amount
    return {"message": "Deposit successful", "saldo": saldo}

@app.post("/saque")
def withdraw(transaction: Transacao):
    global saldo
    if transaction.amount > saldo:
        return {"message": "Insufficient funds", "saldo": saldo}
    saldo -= transaction.amount
    return {"message": "Withdrawal successful", "saldo": saldo}

@app.get("/saldo")
def get_balance():
    return {"saldo": saldo}


