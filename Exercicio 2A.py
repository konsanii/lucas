x1 = float(input("digite a sua primeira nota"))
x2 = float(input("digite a sua segunda nota"))
media = (x1 + x2)/2

if  media >=9.0:
    print("parabens vc foi aprovado suas notas", x1, x2, "sua media", media)

elif  media >=7.5 <9.0:
    print("parabens vc foi aprovado suas notas", x1, x2, "sua media", media)

elif  media >=6.0 <=7.4:
    print("parabens vc foi aprovado suas notas", x1, x2, "sua media", media)

elif  media >=4.0 <=5.9:
    print("lamento vc foi reprovado suas notas", x1, x2, "sua media", media)

elif  media >=0 <3.9:
    print("lamento vc foi reprovado suas notas", x1, x2, "sua media", media)