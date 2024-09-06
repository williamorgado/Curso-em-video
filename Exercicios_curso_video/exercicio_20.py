"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de 
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
e mostre a ordem sorteada.
"""
import random

alunos = []

while True:
    aluno = input(
        'Informe o nome dos alunos ou digite "sair" para finalizar: ')

    if aluno.lower() == "sair":
        break
    else:
        alunos.append(aluno)

random.shuffle(alunos)

print(f'A sequência de aluno a apresentar o trabalho será:\n {alunos}')
