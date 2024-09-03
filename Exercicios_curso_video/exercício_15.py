"""escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
"""
km_rodados = float(input('Informe a quantidade de Km rodados: '))
dias_alugados = int(input('Informe a quantidade de dias alugados: '))

valor_km = km_rodados * 0.15
valor_dias = dias_alugados * 60
valorApagar = valor_dias + valor_km

print(f'O valor a pagar é de: {valorApagar:.2f}')
