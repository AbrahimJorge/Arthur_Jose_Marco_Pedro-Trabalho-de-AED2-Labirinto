"""
Uso desse video para geração aleatória de Labirinto:
https://youtu.be/7wnAcDsckns?si=xRrihxQBu2NFP414

Uso de PDF para auxilio de criação de código de geração aleatória de Labirinto:
file:///C:/Users/Usuario/Downloads/Op%C3%A7%C3%A3o%20de%20problema%202%20-%20Codibentinho%20e%20o%20Labirinto%20(2).pdf

Uso dessa Playlist como auxilio no Pygame
https://youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&si=6Iy9b6YWicib5u85
"""

import pygame
from pygame.locals import *
import random

LARGURA, ALTURA = 640, 640
TELA = pygame.display.set_mode((LARGURA, ALTURA))

TAMANHO_GRADE = 21
TAMANHO_CELULA = LARGURA // TAMANHO_GRADE

#Cores
PRETO = (0, 0, 0)#parede
BRANCO = (255, 255, 255)#caminho
VERDE = (0, 255, 0)#fim

#Geração aleatória d Labirinto
def gerarLabirinto():
    labirinto = [[1] * TAMANHO_GRADE for i in range(TAMANHO_GRADE)]
    
    inicio, fim = (1, 1), (TAMANHO_GRADE - 2, TAMANHO_GRADE - 2)
    labirinto[inicio[1]][inicio[0]] = 0
    labirinto[fim[1]][fim[0]] = 2

    pilha = [inicio]
    
    while pilha:
        x, y = pilha[-1]
        labirinto[y][x] = 0

        vizinhos = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(vizinhos)
        encontrado = False

        for nx, ny in vizinhos:
            if 0 <= nx < TAMANHO_GRADE and 0 <= ny < TAMANHO_GRADE and labirinto[ny][nx]:
                labirinto[ny][nx] = 0
                labirinto[(ny + y) // 2][(nx + x) // 2] = 0
                pilha.append((nx, ny))
                encontrado = True
                break

        if not encontrado:
            pilha.pop()
    
    return labirinto, fim

#Desenhar o Labririnto com as determinadas cores
def desenharLabirinto(labirinto, estado_final):

    for y, linha in enumerate(labirinto):
        for x, celula in enumerate(linha):
            if celula == 1:
                pygame.draw.rect(TELA, PRETO, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
            elif celula == 2:
                pygame.draw.rect(TELA, VERDE, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
            else:
                pygame.draw.rect(TELA, BRANCO, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

    xf, yf = estado_final
    pygame.draw.rect(TELA, VERDE, (xf * TAMANHO_CELULA, yf * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))