import pygame
from pygame.locals import *
from sys import exit
from LabirintoGame import LabirintoGame
from Main import main

#Tela do jogo e titulo
LARGURA, ALTURA = 640, 640
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto")

#Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

def inicio():
    pygame.init()
    iniciar = True
    
    fonte = pygame.font.SysFont("arial", 40, True, False)
    mensagem = 'Pressione SPACE para começar'
    texto_na_tela = fonte.render(mensagem, True, BRANCO)
    fonte2 = pygame.font.SysFont("arial", 30, True, False)
    mensagem2 = 'OBS: Aperte ENTER para ligar ou desligar'
    texto_na_tela2 = fonte2.render(mensagem2, True, BRANCO)
    fonte3 = pygame.font.SysFont("arial", 30, True, False)
    mensagem3 = 'o modo automático'
    texto_na_tela3 = fonte3.render(mensagem3, True, BRANCO)
    
    
    while iniciar:
        TELA.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    iniciar = False
        
        texto_centro = (LARGURA//8, ALTURA//2-30)
        TELA.blit(texto_na_tela, texto_centro)
                      
        texto_centro2 = (LARGURA//8, ALTURA//2 + 50)
        TELA.blit(texto_na_tela2, texto_centro2)     
               
        texto_centro3 = (LARGURA//3, ALTURA//2 + 90)
        TELA.blit(texto_na_tela3, texto_centro3)            
        
        pygame.display.update()
        
    main()

if __name__ == "__main__":
    inicio()