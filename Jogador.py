import pygame
from pygame.locals import *
import sys

LARGURA, ALTURA = 640, 640
TELA = pygame.display.set_mode((LARGURA, ALTURA))

#Cor do personagem
AZUL = (0, 0, 255)

TAMANHO_GRADE = 21
TAMANHO_CELULA = LARGURA // TAMANHO_GRADE

class Jogador:
    def __init__(self, x, y, labirinto):
        self.x = x
        self.y = y
        self.labirinto = labirinto

    def mover(self, dx, dy):
        novo_x = self.x + dx
        novo_y = self.y + dy

        if self.labirinto[novo_y][novo_x] == 0 or (novo_x, novo_y) == self.labirinto[1]:
            self.x = novo_x
            self.y = novo_y
            if (novo_x, novo_y) == self.labirinto[1]:
                print("Você encontrou a saída! O jogo terminou.")
                pygame.quit()
                sys.exit()

    def desenhar(self):
        pygame.draw.rect(TELA, AZUL, (self.x * TAMANHO_CELULA, self.y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))