from matematica import *
from utilidades import *

while True:
    print("digite sair para desligar o sistema")
    menu_operacoes()
    console = input(': ').lower().strip()

    match console:
        case 'sair':
            escolha = menu_saida()
            match escolha:
                case 's':
                    break

                case 'n':
                    continue
        
        case 'soma':
            print('qual tipo de numero usar ?')
            numero_tipo = input('inteiro ou decimal: ').lower().strip()
            if not numero_tipo in ['inteiro', 'decimal']:
                print('entrada inválida ! use as opções no menu')
                print()
                continue

            algoritmo_soma(numero_tipo)
                
        case 'subtração' | 'subtracao':
            print('qual tipo de numero usar ?')
            numero_tipo = input('inteiro ou decimal: ').lower().strip()
            if not numero_tipo in ['inteiro', 'decimal']:
                print('entrada inválida ! use as opções no menu')
                print()
                continue

            algoritmo_subtracao(numero_tipo)
                

        case 'multiplicação' | 'multiplicacao':
            print('qual tipo de numero usar ?')
            numero_tipo = input('inteiro ou decimal: ').lower().strip()
            if not numero_tipo in ['inteiro', 'decimal']:
                print('entrada inválida ! use as opções no menu')
                print()
                continue

            algoritmo_multiplicacao(numero_tipo)
                
        case 'divisão' | 'divisao':
            print('qual tipo de numero usar ?')
            numero_tipo = input('inteiro ou decimal: ').lower().strip()
            if not numero_tipo in ['inteiro', 'decimal']:
                print('entrada inválida ! use as opções no menu')
                print()
                continue

            algoritmo_divisao(numero_tipo)
                
        case 'potencia':
            print('qual tipo de numero usar ?')
            numero_tipo = input('inteiro ou decimal: ').lower().strip()
            if not numero_tipo in ['inteiro', 'decimal']:
                print('entrada inválida ! use as opções no menu')
                print()
                continue

            algoritmo_potencia_positiva(numero_tipo)

        case _:
            print('operação inválida')
            print('use comandos presentes no menu')
            print()

print("Bina software agradece")