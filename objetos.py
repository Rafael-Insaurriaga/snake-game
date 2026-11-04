# Importações

import pygame
import math
import random

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

    posicao_x = 400.0
    posicao_y = 300.0
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
        posicao_x,
        posicao_y,
        velocidade,
        angulo_atual,
        angulo_desejado,
        movendo
    )

# Movimento

def mover_cobra(cabeca,
                posicao_x,
                posicao_y,
                velocidade,
                angulo_atual,
                angulo_desejado,
                movendo):
    
    if not movendo:
        return (
        posicao_x,
        posicao_y,
        cabeca,
        angulo_atual
    )
    
    diferenca = (angulo_desejado - angulo_atual + 180) % 360 - 180

    if abs(diferenca) <= 3:
        angulo_atual = angulo_desejado

    elif diferenca > 0:
        angulo_atual += 3

    elif diferenca < 0:
        angulo_atual -= 3

    angulo_atual %= 360
    angulo_radianos = math.radians(angulo_atual)

    movimento_x = math.cos(angulo_radianos) * velocidade
    movimento_y = math.sin(angulo_radianos) * velocidade

    posicao_x += movimento_x
    posicao_y += movimento_y

    cabeca.x = int(posicao_x)
    cabeca.y = int(posicao_y)

    return (
        posicao_x,
        posicao_y,
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

# Corpo da Cobra

def desenhar_corpo(tela, caminho):
    for x, y in caminho:
        segmento = pygame.Rect(
            x - 10,
            y - 10,
            20,
            20
        )

        pygame.draw.rect(tela, (0, 180, 0), segmento)

def atualizar_corpo(caminho, cabeca, tamanho_corpo):
    caminho.append((cabeca.centerx, cabeca.centery))

    if len(caminho) > tamanho_corpo:
        caminho.pop(0)

    return caminho

# Fruta

def criar_fruta(largura, altura, espessura):
    tamanho = 15

    posicao_x = random.randint(
        espessura,
        largura - espessura - tamanho
    )

    posicao_y = random.randint(
        espessura,
        altura - espessura - tamanho
    )

    fruta = pygame.Rect(
        posicao_x,
        posicao_y,
        tamanho,
        tamanho
    )

    return fruta

def verificar_comida(cabeca, fruta):
    if cabeca.colliderect(fruta):
        return True

    return False

# Colisão

def verificar_colisao_parede(cabeca, borda):

    for parede in borda:

        if cabeca.colliderect(parede):
            return True

    return False

def verificar_colisao_corpo(cabeca, caminho):

    for ponto in caminho[:-20]:

        if cabeca.collidepoint(ponto):
            return True

    return False