import os
os.system('clear')

idade = int(input("Digite a idade:"))
if  idade<=11:
    print("Infantil")
elif idade<=17:
    print("Adolescente")
elif idade<=24:
    print("Jovem")
else:
    print("Adulto")
