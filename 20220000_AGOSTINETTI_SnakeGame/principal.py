import pygame
import constantes
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_comer = pygame.mixer.music.load('munch_1.wav')

x_cobra = int(constantes.LARGURA/2)
y_cobra = int(constantes.ALTURA/2)

x_tamanho = 15
y_tamanho = 15

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(10,470)
y_maca = randint(10,630)

pontos = 0

fonte_arial = pygame.font.SysFont('Arial', 14, True, False)

morreu = False

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
pygame.display.set_caption(constantes.TITULO)
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], x_tamanho, y_tamanho))
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra,y_cobra, lista_cabeca, lista_cobra, x_maca,y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(constantes.LARGURA/2)
    y_cobra = int(constantes.ALTURA/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(10,470)
    y_maca = randint(10,630)
    morreu = False


while True:
    relogio.tick(constantes.FPS)
    tela.fill(constantes.BRANCO)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte_arial.render(mensagem, True, constantes.PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
 

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    if x_cobra < 0:
        print(x_cobra)
        x_cobra = 480

    if x_cobra >480: 
        x_cobra = 0 

    if y_cobra < 0:
        y_cobra = 640

    if y_cobra > 640:
        y_cobra = 0


    cobra = pygame.draw.rect(tela, (constantes.VERDE), (x_cobra, y_cobra, x_tamanho,y_tamanho) )
    maca = pygame.draw.rect(tela,(constantes.VERMELHO), (x_maca,y_maca,15,15))

    if cobra.colliderect(maca):
        x_maca = randint(10,470)
        y_maca = randint(10,630)
        pontos = pontos + 1 
        pygame.mixer.music.play()
        comprimento_inicial = comprimento_inicial +1
        
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca)>1:
        morreu = True
        print('fim de jogo')
      
        while morreu:
            tela.fill(constantes.PRETO)
            mensagem2 = f'Clique r para reinicar a partida'
            texto_formatado2 = fonte_arial.render(mensagem2, True, constantes.BRANCO)

            for event in pygame.event.get():
                if event.type == QUIT:
                 pygame.quit()
                 exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            tela.blit(texto_formatado2, (constantes.LARGURA/2-100,constantes.ALTURA/2))
            pygame.display.update()


    if len(lista_cobra)> comprimento_inicial:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)
    

    tela.blit(texto_formatado, (350,45) )
    pygame.display.update()