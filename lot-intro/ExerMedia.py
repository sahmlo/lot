import os 
os.system('clear')

# Atividade de fixação - Projeto de média.

print('Bem-vindo ao Sistema de Notas e Média.\n')
nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'\nOlá! {nome} sua média foi {media:.1f}')


