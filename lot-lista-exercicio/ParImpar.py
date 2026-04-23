import os
os.system("clear")

numeros = []

for i in range(6):
    n = int(input("Digite um número: "))
    numeros.append(n)

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Lista:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)