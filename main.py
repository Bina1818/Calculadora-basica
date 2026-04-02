import matematica

while True:
    print("Digite sair para desligar o sistema")
    print("Operações: soma, subtração, multiplicação, divisão")
    console = input(': ').lower()
    print()

    if console == 'sair':
        print('Tem certeza que quer desligar o sistema ?')
        escolha = input('s/n: ').lower()

        if escolha == 's':
            break

        elif escolha == 'n':
            continue

        else:
            print("Aviso:[Operação inválida]")
            print('use comandos já presentes no menu')


    elif console == 'soma':
        print("insira os números")
        numero1 = matematica.entrada_numerica('Numero 1')
        numero2 = matematica.entrada_numerica('Numero 2')
        resultado = matematica.soma(numero1, numero2)
        print(f'Resultado = {resultado}')
        print()


    elif console == 'subtração':
        print("insira os números")
        numero1 = matematica.entrada_numerica('Numero 1')
        numero2 = matematica.entrada_numerica('Numero 2')
        resultado = matematica.subtracao(numero1, numero2)
        print(f'Resultado = {resultado}')
        print()


    elif console == 'multiplicação':
        print("insira os números")
        numero1 = matematica.entrada_numerica('Numero 1')
        numero2 = matematica.entrada_numerica('Numero 2')
        resultado = matematica.multiplicacao(numero1, numero2)
        print(f'Resultado = {resultado}')
        print()


    elif console == 'divisão':
        print("insira os números")
        numero1 = matematica.entrada_numerica('Numero 1')
        numero2 = matematica.entrada_numerica('Numero 2')
        resultado = matematica.divisao(numero1, numero2)
        if not resultado is None:
            print(f"Resultado = {resultado}")
        

        else:
            print("Sem resultado")
        print()


    else:
        print("Aviso:[Operação inválida]")
        print('use comandos já presentes no menu')
        print()

print("desenvolvido por Bina Softwares")