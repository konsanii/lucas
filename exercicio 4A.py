x1 = int(input("informe o valor do A"))
if x1>0:
 x2 = int(input("informe o valor do B"))
 x3 = int(input("informe o valor do C"))

 delta = x2**2 - 4*x1*x3

 raiz1 = (-x2 + delta**0.5) /(2/x1 )

 raiz2 = (-x2 - delta**0.5) /(2/x1 )

 if delta <0:
   print("o delta e negativo, a equação não possui raizes reais, o valor de delta é",delta)

 if delta ==0:
  print("o delta e igual a zero logo a equação so tem uma raiz, o valor do delta é", delta ,"e o valor da raiz e", raiz1 )

 if delta >0:
  print("o delta e maior que zero logo tem duas raizes o delta",delta ,"as raizes são" , raiz1 , "positiva," , raiz2 , "negativa.")

else:
 print("o valor do A e igual a zero, logo não e uma equação de segundo grau")