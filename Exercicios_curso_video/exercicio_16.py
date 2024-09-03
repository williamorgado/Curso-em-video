"""
Crie um programa que leia um número real qualquer pelo teclado e mostre
 na tela a sua porção inteira.
"""
import math

numero_real = float(input('Informe um número real qualquer: '))

numero_inteiro = math.trunc(numero_real)

print(f'O número inteiro é: {numero_inteiro}')
