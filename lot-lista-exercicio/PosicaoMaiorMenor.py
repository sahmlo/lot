import os
os.system('cls' or 'clear')

numeros = []

for i in range(5):
    n = float(input("Digite um número: "))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

pos_maior = numeros.index(maior)
pos_menor = numeros.index(menor)

print("Lista:", numeros)
print("Maior valor:", maior, "na posição", pos_maior)
print("Menor valor:", menor, "na posição", pos_menor)