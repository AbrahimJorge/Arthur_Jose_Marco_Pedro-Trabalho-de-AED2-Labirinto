"""
Uso dessa Playlist como auxilio no Pygame
https://youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&si=6Iy9b6YWicib5u85
"""

import pygame
from pygame.locals import *
from Jogador import Jogador
from GerarLab import *
from MovAutomatico import *

class LabirintoGame:
    #Atributos dos Labirinto
    def __init__(self):
        self.labirinto, self.estado_final = gerarLabirinto()
        self.caminho_automatico = a_estrela(self.labirinto, (1, 1), self.estado_final)      
        self.jogador = Jogador(1, 1, self.labirinto)

    #Estado Final
    def verificar_estado_final(self):
        return (self.jogador.x, self.jogador.y) == self.estado_final
    
    #Mover o Jogador com o Modulo Jogador
    def mover_jogador(self, dx, dy):
        novo_x = self.jogador.x + dx
        novo_y = self.jogador.y + dy

        if 0 <= novo_x < TAMANHO_GRADE and 0 <= novo_y < TAMANHO_GRADE and self.labirinto[novo_y][novo_x] == 0:
            self.jogador.x = novo_x
            self.jogador.y = novo_y
            
    #Desenhar Labirinto e Personagem
    def desenhar(self):
        TELA.fill(PRETO)
        desenharLabirinto(self.labirinto, self.estado_final)
        self.jogador.desenhar()
        pygame.display.update()
        
    #Modo Automático com o Modulo MovAutomatico
    def mover_jogador_auto(self):
        if self.caminho_automatico:
            proximo_passo = self.caminho_automatico.pop(0)
            self.jogador.x, self.jogador.y = proximo_passo
            self.automatico = True
            
    #Salvar estado atual do Personagem
    def salvar_estado_atual(self):
        self.caminho_automatico = a_estrela(self.labirinto, (self.jogador.x, self.jogador.y), self.estado_final)