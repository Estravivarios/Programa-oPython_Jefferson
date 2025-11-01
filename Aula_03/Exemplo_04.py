import os
os.system('clear')

idade = int(input("Digite a idade:"))
altura = float(input("Digite a altura da modelo:"))
etnia = input("Digite a etnia da candidata:")

if(idade == 16 and 1.7 and etnia == "indigena"):
    print("Candidata aprovada")
else:
    print("Candidata Reprovada")    
