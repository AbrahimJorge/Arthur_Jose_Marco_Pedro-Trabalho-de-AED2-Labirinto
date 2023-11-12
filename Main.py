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
def ganhar(ganhou, game, texto_centro):
    while ganhou:
        TELA.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_r:
                    main()
                
        texto_centro = (LARGURA//6, ALTURA//2)
        TELA.blit(game, texto_centro)
        pygame.display.update()
        
def main():
    pygame.init()
    jogo = LabirintoGame()
    movimento_automatico = False
    ganhou = False
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                    jogo.mover_jogador(0, -1)
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    jogo.mover_jogador(0, 1)
                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    jogo.mover_jogador(-1, 0)
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    jogo.mover_jogador(1, 0)
                    
                if evento.key == pygame.K_RETURN:
                    movimento_automatico = not movimento_automatico
                    if movimento_automatico:
                        jogo.salvar_estado_atual()

        if movimento_automatico:
            sleep(0.10)
            jogo.mover_jogador_auto()
            
        jogo.desenhar()

        if jogo.verificar_estado_final():
            ganhou = True
            fonte = pygame.font.SysFont("arial", 40, True, False)
            mensagem = 'Pressione R para gerar outro'
            texto_na_tela = fonte.render(mensagem, True, BRANCO)
            centro = texto_na_tela.get_rect
            ganhar(ganhou, texto_na_tela, centro)
        

