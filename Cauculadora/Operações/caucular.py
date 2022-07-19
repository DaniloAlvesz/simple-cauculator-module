while True:
    print("-" * 60)
    print("Olá, seja bem vindo a calculadora sem qualidade.")
    print("-" * 60)
    print("Digite (1) para SOMA")
    print("Digite (2) para SUBTRAÇÃO")
    print("Digite (3) para MULTIPLICAÇÃO")
    print("Digite (4) para DIVISÃO")
    print("-" * 60)
    operador = int(input("Qual operação você deseja fazer? "))
    if operador == 1:
        print("-" * 60)
        print("SOMA---")
        n1 = float(input("Digite um número a ser somado: "))
        n2 = float(input("Digite outro número a ser somado: "))
        print("_"*50)
        print("O resultado da soma é: {}".format(n1+n2))
        print("_"*50)
    elif operador == 2: 
        print("-" * 60)
        print("SUBTRAÇÃO----")
        n1 = float(input("Digite um número a ser subtraido: "))
        n2 = float(input("Digite outro número a ser subtraido: "))
        print("_"*50)
        print("O resultado da subtração é: {}".format(n1-n2))
        print("_"*50)
    elif operador == 3: 
        print("-" * 60)
        print("Multiplicação****")
        n1 = float(input("Digite um número a ser multiplicado: "))
        n2 = float(input("Digite outro número a ser multiplicado: "))
        print("_"*50)
        print("O resultado da multiplicação é: {}".format(n1*n2))
        print("_"*50)
    elif operador == 4: 
        print("-" * 60)
        print("Divisão****")
        n1 = float(input("Digite um número a ser dividido: "))
        n2 = float(input("Digite outro número a ser dividido: "))
        print("_"*50)
        print("O resultado da divisão é: {}".format(n1/n2))
        print("_"*50)
    print("o que você deseja fazer agora? ")
    print("-" * 60)
    print("1 - Voltar ao inicio")
    print("2 - Terminar")
    print("-" * 60)
    desejo = int(input(": "))
    while True:
        if desejo == 1:
            break
        if desejo == 2:
            break
        else:
            print("Ops, Digite uma opção valida")
    if desejo == 2:
        print("Obrigado por usar a cauculadora sem qualidade.")
        break   
    else: 
        print("Digite uma oção valida: ")