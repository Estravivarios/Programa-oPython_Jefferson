import os
os.system('clear')

valor = float(input("Digite o valor do produto:R$"))
if valor<=20:
    venda = valor+(valor*0.45)
else:
    venda = valor+(valor*0.45)
    print("o Valor para venda é:R$ ",venda)
    