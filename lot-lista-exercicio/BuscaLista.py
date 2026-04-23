import os
os.system("cls" or "clear")

numeros = []

for i in range(len(numeros)):
    if numeros[i] == busca:
        print(f"Encontrado na posição {i}")
        break
busca = int(input("Digite um número para buscar: "))

if busca in numeros:
    print("Número encontrado!")
    print(f"Encontrado na posição {numeros.index(busca)}")
else:
    print("Número não encontrado.")

print("Lista:", numeros)