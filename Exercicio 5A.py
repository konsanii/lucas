ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Este é um ano bissexto")
        else:
            print("Este não é um ano bissexto")
    else:
        print("Este é um ano bissexto")
else:
    print("Este não é um ano bissexto")