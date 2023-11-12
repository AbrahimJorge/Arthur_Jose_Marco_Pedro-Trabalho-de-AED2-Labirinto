import pygame
from pygame.locals import *
from sys import exit
from LabirintoGame import LabirintoGame
from Main import main

#Tela do jogo e titulo
LARGURA, ALTURA = 640, 640
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto")

def inicio():
    pygame.init()
    iniciar = True
    
    imagem_fundo = pygame.image.load("Telas/TelaInicio.png").convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    while iniciar:
        #TELA.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    iniciar = False     
        
        TELA.blit(imagem_fundo, (0, 0))
        pygame.display.update()
        
    main()

if __name__ == "__main__":
    inicio()