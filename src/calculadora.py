def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha(1/2/3/4): ")

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif escolha == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif escolha == '3':
        print(num1, "*", num2, "=", num1 * num2

    elif escolha == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Erro! Divisão por zero não é permitida.")

    else:
        print("Entrada Inválida")

calculadora()
