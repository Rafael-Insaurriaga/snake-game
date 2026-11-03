# Importações

import pygame

# Obstáculos

def criar_borda(largura, altura, espessura):

    parede_superior = pygame.Rect(
        0,
        0,
        largura,
        espessura
    )

    parede_inferior = pygame.Rect(
        0,
        altura - espessura,
        largura,
        espessura
    )

    parede_esquerda = pygame.Rect(
        0,
        0,
        espessura,
        altura
    )

    parede_direita = pygame.Rect(
        largura - espessura,
        0,
        espessura,
        altura
    )

    borda = [
        parede_superior,
        parede_inferior,
        parede_esquerda,
        parede_direita
    ]

    return borda

# Cobra

def criar_cobra():

    tamanho = 20

    posicao_x = 400
    posicao_y = 300
    velocidade = 1
    movendo = False

    angulo_atual = 0
    angulo_desejado = 0

    cabeca = pygame.Rect(
        posicao_x,
        posicao_y,
        tamanho,
        tamanho
    )

    return (
        cabeca,
        velocidade,
        angulo_atual,
        angulo_desejado,
        movendo
    )

# Movimento

def mover_cobra(cabeca,
                velocidade,
                angulo_atual,
                angulo_desejado,
                movendo):

    if not movendo:
        return (
            cabeca,
            angulo_atual
        )

    if angulo_desejado == 0:
        cabeca.x += velocidade

    elif angulo_desejado == 90:
        cabeca.y += velocidade

    elif angulo_desejado == 180:
        cabeca.x -= velocidade

    elif angulo_desejado == 270:
        cabeca.y -= velocidade

    angulo_atual = angulo_desejado

    return (
        cabeca,
        angulo_atual
    )

# Controle da Cobra

def controlar_cobra(angulo_desejado, movendo):

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        angulo_desejado = 0
        movendo = True

    elif teclas[pygame.K_DOWN]:
        angulo_desejado = 90
        movendo = True

    elif teclas[pygame.K_LEFT]:
        angulo_desejado = 180
        movendo = True

    elif teclas[pygame.K_UP]:
        angulo_desejado = 270
        movendo = True

    return ( angulo_desejado, 
            movendo
    )