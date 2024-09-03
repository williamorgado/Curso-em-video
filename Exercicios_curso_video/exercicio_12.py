"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
    com 5% de desconto
"""

# valor do produto
valor_real = float(input('Informe o valor do produto: R$ '))

# valor do desconto
valor_desconto = valor_real - ((valor_real * 5) / 100)

# imprimindo o valor
print(f"O valor com desconto é: {valor_desconto}")
