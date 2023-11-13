"""
Uso dessa Playlist como auxilio no Pygame
https://youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&si=6Iy9b6YWicib5u85
"""

import pygame
from pygame.locals import *
from sys import exit
from LabirintoGame import LabirintoGame
from time import sleep

#Tela do jogo e titulo
LARGURA, ALTURA = 640, 640
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto")

#Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

#Essa função só vai aparecer quando achar o final
def ganhar(ganhou):
    imagem_fundo = pygame.image.load("Telas/final.png").convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    while ganhou:
        TELA.fill((0,0,0))
        for event in pygame.event.get():
            #Se ele apertou para sair fecha o jogo
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            #Gerar um novo labirinto
            if event.type == KEYDOWN:
                if event.key == K_r:
                    main()

        TELA.blit(imagem_fundo, (0,0))
        pygame.display.update()
        
#Função para rodar o jogo
def main():
    pygame.init()
    movimento_automatico = False
    jogo = LabirintoGame()
    ganhou = False
    
    while True:
        for evento in pygame.event.get():
            #Se ele apertou para sair fecha o jogo
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            #Verificação de botão para movimento
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    jogo.mover_jogador(0, -1)
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    jogo.mover_jogador(0, 1)
                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    jogo.mover_jogador(-1, 0)
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    jogo.mover_jogador(1, 0)
                    
                #Botão do modo automático
                if evento.key == pygame.K_RETURN:
                    movimento_automatico = not movimento_automatico
                    if movimento_automatico:
                        jogo.salvar_estado_atual()
                        
        #Ligar o modo automático
        if movimento_automatico:
            sleep(0.10)
            jogo.mover_jogador_auto()
            
        #Desenhar os Sprites
        jogo.desenhar()
        
        #Verificar a vitoria
        if jogo.verificar_estado_final():
            ganhou = True
            ganhar(ganhou)
        

