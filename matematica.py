# [operações matemáticas]
# funções utilizadas para cálculos 

def soma(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    return valor1 - valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2


def divisao_inteira(valor1, valor2):
    if valor2 == 0:
        print("Aviso:[Divisão por zero]")
        print('Processo cancelado para evitar erro')
        return
    
    return valor1 // valor2

def divisao_decimal(valor1, valor2):
        if valor2 == 0:
            print("Aviso:[Divisão por zero]")
            print('Processo cancelado para evitar erro')
            return
    
        return valor1 / valor2


def potencia_positiva(base, expoente):
    if expoente == 0:
        return 1

    resultado = base

    for _ in range(expoente-1):
        resultado = multiplicacao(resultado * base)
    return resultado


# [variados]
# funções não de cálculo porém usadas para fins matemáticos

def entrada_numerica(mensagem):
    while True:
        try: 
            numero = int(input(f'{mensagem} '))
        except ValueError:
           print("Erro: insira um número inteiro !")
           continue
    
        return numero


def entrada_flutuante(mensagem):
    while True:
        try: 
            numero = float(input(f'{mensagem} '))
        except ValueError:
           print("Erro: insira um número inteiro !")
           continue
    
        return numero

def entrada_repetida(entrada_tipo, vezes):
    valores = []
    for _ in range(vezes):
        valor = entrada_tipo('Digite:')
        valores.append(valor)
    return valores