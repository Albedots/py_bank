import datetime  # import das bibliotecas
# declaração dos campos dos saques diarios
saques_dia = 0
data_ultimo_saque = datetime.date.today()
hoje = datetime.date.today()

saldo = ...
# declaração dos campos saldo e valor
valor = ...


def deposito():  # função para deposito
    global saldo, valor

    if valor > 0 and saldo >= 0:  # condicional que soma valor com saldo e retorna float com 2 casas decimais
        saldo += valor
        return round(float(saldo), 2)
    
    elif valor < 0:
       return "valor invalido"
    

def saque():  # função para saque
    global saldo, valor, saques_dia, data_ultimo_saque, hoje
    while saques_dia < 4:
        if hoje != data_ultimo_saque:  # verifica o dia do ultimo saque e caso seja outro dia, zera o contador
            saques_dia = 0
            data_ultimo_saque = hoje

        if saques_dia >= 3:
            return "Número máximo de saques por dia atingido!"

        elif saldo >= 0 and valor > 0 and valor < saldo and valor <= 500:  # condicional que subtrai o valor do saldo
            saldo -= valor
            saques_dia += 1  #  contador de saques diarios
            return round(float(saldo), 2)

        elif valor > saldo:
            return "Valor de saque maior que saldo!"

        elif valor > 500:
            return "Valor máximo por saque atingido!"

        else:
            return "Valor inválido para saque."