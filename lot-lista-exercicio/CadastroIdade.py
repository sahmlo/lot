import os
os.system('cls' or 'clear')

idades = []
maiores_18 = 0

while True:
    idade = int(input("Digite uma idade (-1 para sair): "))

    if idade == -1:
        break
    else:
        idades.append(idade)

for i in idades:
    
    if i >= 18:
        maiores_18 += 1
        
media = sum(idades) / len(idades)

print("Lista:", idades)
print("Média:", media)
print("Maiores ou iguais a 18:", maiores_18)