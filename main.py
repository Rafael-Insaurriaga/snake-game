# Importações

import pygame
import random

from objetos import criar_borda
from objetos import criar_cobra
from objetos import controlar_cobra
from objetos import mover_cobra

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

cabeca, velocidade, angulo_atual, angulo_desejado, movendo = criar_cobra()

# Funções

def desenhar_mapa():

    tela.fill(PRETO)

    for parede in borda:
        pygame.draw.rect(tela, BRANCO, parede)
        pygame.draw.rect(tela, BRANCO, cabeca)
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

    cabeca, angulo_atual = mover_cobra(
        cabeca,
        velocidade,
        angulo_atual,
        angulo_desejado,
        movendo
    )

    # Desenho

    desenhar_mapa()

    pygame.display.update() 