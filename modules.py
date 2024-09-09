import datetime

saques_dia = 0
data_ultimo_saque = datetime.date.today()
hoje = datetime.date.today()

saldo = ...

valor = ...


def deposito():
    global saldo, valor

    if valor > 0 and saldo >= 0:
        saldo += valor
        return round(float(saldo), 2)
    
    elif valor < 0:
       return "valor invalido"
    

def saque():
    global saldo, valor, saques_dia, data_ultimo_saque, hoje
    while saques_dia < 4:
        if hoje != data_ultimo_saque:  # verifica o dia do ultimo saque e caso seja outro dia, zera o contador
            saques_dia = 0
            data_ultimo_saque = hoje

        if saques_dia >= 3:
            return "Número máximo de saques por dia atingido!"

        elif saldo >= 0 and valor > 0 and valor < saldo and valor <= 500:
            saldo -= valor
            saques_dia += 1
            return round(float(saldo), 2)

        elif valor > saldo:
            return "Valor de saque maior que saldo!"

        elif valor > 500:
            return "Valor máximo por saque atingido!"

        else:
            return "Valor inválido para saque."