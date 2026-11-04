# Importações

import pygame
import random

from objetos import criar_borda
from objetos import criar_cobra
from objetos import controlar_cobra
from objetos import mover_cobra
from objetos import desenhar_corpo
from objetos import atualizar_corpo
from objetos import criar_fruta
from objetos import verificar_comida

# Inicialização

pygame.init()

# Cores

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Configurações

largura = 800
altura = 600
espessura = 10

# Janela

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

borda = criar_borda(largura, altura, espessura)

cabeca, posicao_x, posicao_y, velocidade, angulo_atual, angulo_desejado, movendo = criar_cobra()

fruta = criar_fruta(largura, altura, espessura)

caminho = []
tamanho_corpo = 0
crescimento = 0

# Funções

def desenhar_mapa():

    tela.fill(PRETO)

    for parede in borda:
        pygame.draw.rect(tela, BRANCO, parede)

    desenhar_corpo(tela, caminho)
    pygame.draw.rect(tela, BRANCO, cabeca)

    pygame.draw.rect(tela, (255, 0, 0), fruta)

# Variáveis

rodando = True

# Loop

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Controle

    angulo_desejado, movendo = controlar_cobra(
        angulo_desejado, 
        movendo
    )

    # Movimento

    posicao_x, posicao_y, cabeca, angulo_atual = mover_cobra(
    cabeca,
    posicao_x,
    posicao_y,
    velocidade,
    angulo_atual,
    angulo_desejado,
    movendo
    )
    
    caminho = atualizar_corpo(
    caminho,
    cabeca,
    tamanho_corpo
    )

    if verificar_comida(cabeca, fruta):
        fruta = criar_fruta(largura, altura, espessura)
        crescimento += 20

    if crescimento > 0:
        tamanho_corpo += 1
        crescimento -= 1

    desenhar_mapa()

    pygame.display.update() 