"""Criando um programa que toca música
"""

import pygame

# Iniciar o mixer do pygame
pygame.mixer.init()
# carregar o aquivo de música
pygame.mixer.music.load('Exercicios_curso_video/BLANK_Get Up.mp3')
# reproduzir a música
pygame.mixer.music.play()

# mantém o programa rodando até a múscica acabar
input('Aperte Enter para parar a música...')
pygame.mixer.music.stop()
