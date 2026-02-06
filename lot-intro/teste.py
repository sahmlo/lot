import os 
os.system("clear || cls")

# introdução à lot - Projeto de Supermercado
# Supermercado da Barbie

print('Bem-vindo ao Supermercado da Barbie Nordestina.\n')

feijao = 4.00
arroz = 3.00
macarrao = 2.00
vinho = 50.36
acucar = 3.50

qtd_feijao = int(input("Digite a quantidade de feijão: "))
qtd_arroz = int(input("Digite a quantidade de arroz: "))
qtd_macarrao = int(input("Digite a quantidade de macarrão: "))
qtd_vinho = int(input("Digite a quantidade de vinho: "))
qtd_acucar = int(input("Digite a quantidade de açúcar: \n"))

print("Calculando o valor total da compra...\n")
total = (feijao * qtd_feijao) + (arroz * qtd_arroz) + (macarrao * qtd_macarrao) + (vinho * qtd_vinho) + (acucar * qtd_acucar)
print(f"O valor total da compra é: R$ {total:.2f}\n")
print('Obrigado pela preferência. Volte Sempre! Oxalá é Fiel.')