"""Faça um programa que leia a largura e a altura de uma parede em metros,
    calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que
    cada litro de tinta, pinta uma área de 2m²
    cada litro de tinta pinta 2m².
 """




# altura da parede
altura = float(input("Informe a altura da parede em metros: "))

# largura da parede
largura = float(input("Informe a largura da parede em metros: "))

# calcula a área da parede
area = altura * largura

# calcula a quantidade de tinta necessária (1l por 2m²)
litros_tinta = area/2

print(f'Você vai precisar de {litros_tinta:.2f} litros de tinta')
