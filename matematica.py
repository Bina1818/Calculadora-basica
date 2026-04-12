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
        print("divisão por zero !")
        print('processo cancelado para evitar erro')
        return None
    
    return valor1 // valor2

def divisao_decimal(valor1, valor2):
        if valor2 == 0:
            print("divisão por zero !")
            print('processo cancelado para evitar erro')
            return None
    
        return valor1 / valor2

def potencia_positiva(base, expoente):
    if expoente == 0:
        return 1

    resultado = base

    for _ in range(expoente-1):
        resultado = resultado * base
    return resultado


# [variados]
# funções não de cálculo porém usadas para fins matemáticos

def entrada_inteira(mensagem = 'digite um número inteiro:'):
    while True:
        try: 
            numero = int(input(f'{mensagem} '))
        except ValueError:
           print("inválido: insira um número inteiro !")
           continue
    
        return numero

def entrada_flutuante(mensagem = 'digite um número decimal:'):
    while True:
        try: 
            numero = float(input(f'{mensagem} '))
        except ValueError:
           print("inválido: insira um número decimal !")
           continue
    
        return numero

def entrada_repetida(entrada_tipo, vezes):
    valores = []
    for _ in range(vezes):
        valor = entrada_tipo()
        valores.append(valor)
    return valores

#[templates]
# códigos prontos para uso

def algoritmo_soma(numero_tipo):
    if numero_tipo == 'inteiro':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_inteira, vezes=2)
        resultado = soma(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    elif numero_tipo == 'decimal':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_flutuante, vezes=2)
        resultado = soma(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    else:
        print('tipo númerico não válido')
        return None

def algoritmo_subtracao(numero_tipo):
    if numero_tipo == 'inteiro':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_inteira, vezes=2)
        resultado = subtracao(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    elif numero_tipo == 'decimal':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_flutuante, vezes=2)
        resultado = subtracao(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    else:
        print('tipo númerico não válido')
        return None

def algoritmo_multiplicacao(numero_tipo):
    if numero_tipo == 'inteiro':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_inteira, vezes=2)
        resultado = multiplicacao(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    elif numero_tipo == 'decimal':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_flutuante, vezes=2)
        resultado = multiplicacao(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    else:
        print('tipo númerico não válido')
        return None

def algoritmo_divisao(numero_tipo):
    if numero_tipo == 'inteiro':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_inteira, vezes=2)
        resultado = divisao_inteira(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    elif numero_tipo == 'decimal':
        print("insira os valores")
        numeros = entrada_repetida(entrada_tipo=entrada_flutuante, vezes=2)
        resultado = divisao_decimal(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    else:
        print('tipo númerico não válido')
        return None

def algoritmo_potencia_positiva(numero_tipo):
    if numero_tipo == 'inteiro':
        print('primeiro argumento é a base e segundo o expoente')
        numeros = entrada_repetida(entrada_tipo=entrada_inteira, vezes=2)
        resultado = potencia_positiva(numeros[0], numeros[1])
        print(f'resultado = {resultado}')

    elif numero_tipo == 'decimal':
        print('primeiro argumento é a base e segundo o expoente')
        numeros = entrada_repetida(entrada_tipo=entrada_flutuante, vezes=2)
        resultado = potencia_positiva(numeros[0], numeros[1])
        print(f'resultado = {resultado}')
    
    else:
        print('tipo númerico não válido')