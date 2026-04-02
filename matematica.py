# [operações matemáticas]
# funções utilizadas para cálculos 

def soma(valor1: int, valor2: int) -> int:
    return valor1 + valor2


def subtracao(valor1: int, valor2: int) -> int:
    return valor1 - valor2


def multiplicacao(valor1: int, valor2: int) -> int:
    return valor1 * valor2


def divisao(valor1: int, valor2: int) -> int:
    if valor2 == 0:
        print("Aviso:[Divisão por zero]")
        print('Processo cancelado para evitar erro')
        return
    
    return valor1 // valor2


def potencia_positiva(base: int, expoente: int) -> int:
    if expoente == 0:
        return 1

    resultado = base

    for i in range(expoente-1):
        resultado = resultado * base
    return resultado


# [variados]
# funções não de cálculo porém usadas para fins matemáticos

def entrada_numerica(mensagem: str) -> int:
    while True:
        try: 
            numero = int(input(f'{mensagem} '))
        except ValueError:
           print("Erro: insira um número inteiro !")
           continue
    
        return numero


def entrada_flutuante(mensagem: str) -> int:
    while True:
        try: 
            numero = float(input(f'{mensagem} '))
        except ValueError:
           print("Erro: insira um número inteiro !")
           continue
    
        return numero