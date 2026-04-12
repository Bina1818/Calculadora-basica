#[funções diversas]
# recursos com usos váriados
def menu_operacoes():
    print('Operações disponíveis')
    print("Soma")
    print("Subtração")
    print("Multiplicação")
    print("Divisão")
    print("Potencia")
    print()

def menu_saida():
    while True:
        print("tem certeza que quer desligar o sistema ?")
        escolha = input('s/n: ').lower().strip()

        match escolha:
            case 's':
                return 's'

            case 'n':
                return 'n'

            case _:
                print('inválido, use o menu !')
                print()
                continue