import random
numero_aleatorio = random.randint(0, 100)
print(numero_aleatorio) 
tentativas = 0
while True:
    x = int(input("Adivinhe o número: "))
    tentativas += 1
    if numero_aleatorio < x:
        print("É menor!")
    elif numero_aleatorio > x:
        print("É maior!")
    else:
        print(f"Você acertou em {tentativas} tentativas!")
        break