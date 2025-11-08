import os
os.system('clear')

salario = float(input("Digite seu salario:"))
if salario<=600:
    print("isento")
elif salario<=1200:
    print("DescontosINSS:20%")
elif salario<=2000:
    print("DescontoINSS:25%")
else:
    print("DescontoINSS:30%")
            


