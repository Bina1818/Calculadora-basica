from matematica import *

while True:
    print("Digite sair para desligar o sistema")
    print("Operações: soma, subtração, multiplicação, divisão inteira, divisão decimal")
    console = input(': ').lower()
    print()

    match console:
        case 'sair':
            print('tem de que quer desligar o sistema ?')
            escolha = input('s/n: ').lower().strip()

            match escolha:
                case 's':
                    break

                case 'n':
                    continue

                case _:
                    print('AVISO:[entrada inválida]')
                    print('use comandos já presentes no menu')
        
        case 'soma':
            numeros = entrada_repetida(entrada_tipo=entrada_numerica, vezes=2)
            resultado = soma(numeros[0], numeros[1])
            print(f'Resultado = {resultado}')
                
        case 'subtração':
            numeros = entrada_repetida(entrada_tipo=entrada_numerica, vezes=2)
            resultado = subtracao(numeros[0], numeros[1])
            print(f'Resultado = {resultado}')
        
        case 'multiplicação':
            numeros = entrada_repetida(entrada_tipo=entrada_numerica, vezes=2)
            resultado = multiplicacao(numeros[0], numeros[1])
            print(f'Resultado = {resultado}')
        
        case 'divisão':
            print('AVISO:[operação inválida]')
            print('operação de divisão deve ser especificada')
        
        case 'divisão inteira':
            numeros = entrada_repetida(entrada_tipo=entrada_numerica, vezes=2)
            resultado = divisao_inteira(numeros[0], numeros[1])
            if resultado is None:
                print("Sem resultado")
                continue

            print(f'Resultado = {resultado}')

        case 'divisão decimal':
            numeros = entrada_repetida(entrada_tipo=entrada_numerica, vezes=2)
            resultado = divisao_decimal(numeros[0], numeros[1])
            if resultado is None:
                print('Sem resultado')
                continue

            print(f'Resultado = {resultado}')


        
        case _:
            print('AVISO[operação inválida]')
            print('use comandos presentes no menu')

print("Bina software agradece")