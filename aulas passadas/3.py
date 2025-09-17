x = 0
y = 0
porta = ""

while porta != "sair":
    x = float(input("Digite seu primeiro número: "))
    y = float(input("Digite seu segundo número: "))

    sinais = input(f"Você digitou os números {x} e {y}. Escolha se vai somar (1) ou multiplicar (2): ")

    if sinais == "1":
        resposta = x + y
        print(f"Sua soma é: {resposta}")
    elif sinais == "2":
        resposta2 = x * y
        print(f"Sua multiplicação é: {resposta2}")
    else:
        print("Opção inválida!")

    porta = input("Digite 'sair' para encerrar ou pressione Enter para continuar: ")