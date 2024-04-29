numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("O número fornecido não é menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10

    print("Centenas:", centenas)
    print("Dezenas:", dezenas)
    print("Unidades:", unidades)

