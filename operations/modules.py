"""DOC
 Esse documento exemplifica as regras Lógicas funcionais e de negócios que
 a aplicação deve seguir
"""

import datetime

# Inicializa os campos relacionados aos saques diários
saques_dia = 0  # Contador para o número de saques realizados no dia
data_ultimo_saque = datetime.date.today()  # Armazena a data do último saque realizado
hoje = datetime.date.today()  # Data atual

saldo = ...  # Saldo atual da conta (deve ser definido e inicializado adequadamente)
valor = ...  # Valor a ser depositado ou sacado (deve ser definido e inicializado adequadamente)

def deposito():
    """
    Realiza um depósito na conta.

    Requisitos Funcionais:
    - O depósito deve ser realizado somente se o valor for positivo.
    - O saldo deve ser atualizado corretamente.
    - O saldo deve ser retornado com duas casas decimais.

    Regras de Negócio:
    - O valor de depósito deve ser positivo.
    - O saldo deve ser maior ou igual a zero antes do depósito.

    Returns:
    float: O saldo atualizado com duas casas decimais se o valor do depósito for válido.
    str: Uma mensagem de erro "valor inválido" se o valor do depósito for negativo.
    """
    global saldo, valor

    if valor > 0 and saldo >= 0:
        saldo += valor
        return round(float(saldo), 2)
    elif valor < 0:
        return "valor invalido"


def saque():
    """
    Realiza um saque da conta.

    Requisitos Funcionais:
    - O saque deve ser realizado somente se o valor for positivo e menor que o saldo.
    - O valor do saque deve ser menor ou igual a 500.
    - O número de saques diários é limitado a 3.
    - O contador de saques é reiniciado a cada novo dia.

    Regras de Negócio:
    - O valor do saque deve ser positivo e menor que o saldo da conta.
    - O valor do saque não pode exceder 500.
    - O número máximo de saques permitidos por dia é 3.

    Returns:
    float: O saldo atualizado com duas casas decimais se o saque for bem-sucedido.
    str: Mensagens de erro específicas:
        - "Número máximo de saques por dia atingido!" se o limite diário for alcançado.
        - "Valor de saque maior que saldo!" se o valor solicitado for maior que o saldo.
        - "Valor máximo por saque atingido!" se o valor solicitado exceder o limite permitido.
        - "Valor inválido para saque." se o valor do saque não atender aos critérios.
    """
    global saldo, valor, saques_dia, data_ultimo_saque, hoje

    if hoje != data_ultimo_saque:
        saques_dia = 0
        data_ultimo_saque = hoje

    if saques_dia >= 3:
        return "Número máximo de saques por dia atingido!"

    if saldo >= 0 and valor > 0 and valor < saldo and valor <= 500:
        saldo -= valor
        saques_dia += 1
        return round(float(saldo), 2)

    elif valor > saldo:
        return "Valor de saque maior que saldo!"
    elif valor > 500:
        return "Valor máximo por saque atingido!"
    else:
        return "Valor inválido para saque."
