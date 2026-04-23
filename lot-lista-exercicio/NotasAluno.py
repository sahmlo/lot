import os
os.system('cls' or 'clear')

notas = []

def calcular_media(notas):
    return sum(notas) / len(notas)

while len(notas) < 5:
    nota = float(input('Digite a nota do aluno (0-10): '))
    
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print('Nota inválida. Digite uma nota entre 0 e 10.')
        
media = calcular_media(notas)

acima= 0
abaixo = 0

for nota in notas:
    if nota >= media:
        acima += 1
    else:
        abaixo += 1
        
print(f'Média das notas: {media:.2f}')
print(f'Quantidade acima ou igual à média: {acima}')
print(f'Quantidade abaixo da média: {abaixo}')