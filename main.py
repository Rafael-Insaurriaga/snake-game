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
from objetos import verificar_colisao_parede
from objetos import verificar_colisao_corpo
from objetos import carregar_imagem
from objetos import TAMANHO_COBRA, TAMANHO_FRUTA, ORIENTACAO_CABECA
from objetos import carregar_recorde, salvar_recorde

# Inicialização

pygame.init()
clock = pygame.time.Clock()

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

sprite_cabeca = carregar_imagem("cabeca.png", (TAMANHO_COBRA, TAMANHO_COBRA))
sprite_corpo = carregar_imagem("corpo.png", (TAMANHO_COBRA, TAMANHO_COBRA))
sprite_fruta = carregar_imagem("fruta.png", (TAMANHO_FRUTA, TAMANHO_FRUTA))

borda = criar_borda(largura, altura, espessura)

cabeca, posicao_x, posicao_y, velocidade, angulo_atual, angulo_desejado, movendo = criar_cobra()

fruta = criar_fruta(largura, altura, espessura)

caminho = []
tamanho_corpo = 0
crescimento = 0
contador_crescimento = 0
pontos = 0
recorde = carregar_recorde()

# Funções

def desenhar_mapa(perdeu, pontos, recorde):

    tela.fill(PRETO)

    for parede in borda:
        pygame.draw.rect(tela, BRANCO, parede)

    desenhar_corpo(tela, caminho, sprite_corpo, cabeca)

    imagem_cabeca = pygame.transform.rotate(sprite_cabeca, ORIENTACAO_CABECA - angulo_atual)
    tela.blit(imagem_cabeca, imagem_cabeca.get_rect(center=cabeca.center))

    tela.blit(sprite_fruta, fruta)

    fonte = pygame.font.SysFont(None, 36)

    texto_pontos = fonte.render(
    f"Pontos: {pontos}",
    True,
    (180, 180, 180)
)

    texto_pontos.set_alpha(180)

    retangulo = texto_pontos.get_rect(
    center=(largura // 2, 30)
)

    tela.blit(texto_pontos, retangulo)

    texto_recorde = fonte.render(
        f"Recorde: {recorde}",
        True,
        (180, 180, 180)
    )

    texto_recorde.set_alpha(180)

    tela.blit(
        texto_recorde,
        texto_recorde.get_rect(center=(largura // 2, altura - 30))
    )

    if perdeu:

        fonte = pygame.font.SysFont(None, 50)

        texto = fonte.render(
        "GAME OVER",
        True,
        (BRANCO)
    )

        tela.blit(texto, (280, 250))

        fonte_pequena = pygame.font.SysFont(None, 28)

        texto_reiniciar = fonte_pequena.render(
             "Pressione R para reiniciar",
             True,
            BRANCO
    )

        tela.blit(texto_reiniciar, (265, 305))

# Variáveis

rodando = True
perdeu = False

# Loop

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    teclas = pygame.key.get_pressed()

    # Controle

    angulo_desejado, movendo = controlar_cobra(
        angulo_desejado, 
        movendo
    )

    # Movimento
    if not perdeu:
        passos = 1

        if teclas[pygame.K_SPACE]:
            passos = 5   # dash: 5 passos de 1px por frame

        for i in range(passos):
            posicao_x, posicao_y, cabeca, angulo_atual = mover_cobra(
                cabeca,
                posicao_x,
                posicao_y,
                velocidade,
                angulo_atual,
                angulo_desejado,
                movendo,
                girar=(i == 0)   
            )

            if verificar_colisao_parede(cabeca, borda):
                perdeu = True

            if verificar_colisao_corpo(cabeca, caminho):
                perdeu = True

            if perdeu:
                break

            caminho = atualizar_corpo(
                caminho,
                cabeca,
                tamanho_corpo
            )

            if verificar_comida(cabeca, fruta):
                fruta = criar_fruta(largura, altura, espessura)
                crescimento += 2    # era 20: metade, pra testar
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
                
        # fora do for: roda 1 vez por frame, com ou sem dash
        if crescimento > 0:
            contador_crescimento += 1

            if contador_crescimento >= (TAMANHO_COBRA // 2) / velocidade:
                contador_crescimento = 0
                tamanho_corpo += 1
                crescimento -= 1

        if perdeu:
            salvar_recorde(recorde)        

    if perdeu and teclas[pygame.K_r]:

        cabeca, posicao_x, posicao_y, velocidade, angulo_atual, angulo_desejado, movendo = criar_cobra()

        fruta = criar_fruta(largura, altura, espessura)

        caminho = []

        tamanho_corpo = 0

        crescimento = 0

        contador_crescimento = 0

        pontos = 0

        perdeu = False

    desenhar_mapa(perdeu, pontos, recorde)

    pygame.display.update() 
    clock.tick(60)

salvar_recorde(recorde)
pygame.quit()