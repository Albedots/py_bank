saldo = ...

valor = ...

def deposito():
    global saldo, valor

    if valor > 0 and saldo >= 0:
        resultado = float(valor + saldo)
        return round(resultado, 2)
    
    elif valor < 0:
       return "valor invalido"
    