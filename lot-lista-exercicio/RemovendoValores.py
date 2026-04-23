import os
os.system('cls' or 'clear')

numeros = []

for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    
positivo = []

for numero in numeros:
    if numero > 0:
        positivo.append(numero)
        
removidos = len(numeros) - len(positivo)

print("Lista original:", numeros)
print("Lista sem os números negativos:", positivo)
print("Quantidade de números removidos:", removidos)