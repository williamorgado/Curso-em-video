"""Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo
 salário, com 15% de aumento
"""

salario_atual = float(input("Informe seu salário atual: "))

salario_novo = salario_atual + ((salario_atual * 15) / 100)

print(f'Seu salário com aumento fica de: {salario_novo:.2f}')
