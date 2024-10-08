"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
o nome do escolhido.
"""
import random

# armazenando os nomes dos alunos
alunos = []

while True:
    aluno = input('Digite o nome do aluno ou "sair" para finalizar: ')

    if aluno.lower() == "sair":
        break
    else:
        alunos.append(aluno)

if alunos:
    nome_sorteado = random.choice(alunos)
    print(f'O aluno sorteado foi {nome_sorteado.capitalize()}')
else:
    print('Nenhum aluno foi inserido.')
