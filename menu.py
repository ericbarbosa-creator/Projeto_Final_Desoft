# Importando as bibliotecas necessárias.
import pygame
from os import path

# Dados gerais do jogo.
TITULO = 'Aprendiz de feiticeiro'
WIDTH = 700 # Largura da tela
HEIGHT = 300 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a sequência de textos
MENUS = {
    'Principal': ['Treino', 'Duelo', 'Sair'],
    'Treino': [
        'Você é novato na escola para feiticeiros e por isso precisa treinar,',
        'principalmente a mira de sua varinha,por isso treine acertando o maximo de mostros que você puder.',],
    'Duelo': ['Você ja esta pronto para duelar!! Agora mostre do que você é capaz.',],
    'Sair': [''],
}

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega a fonte padrão do sistema
    font = pygame.font.SysFont(None, 16)

    # Vamos utilizar esta variável para controlar o texto a ser mostrado
    text_index = 0
    game = True
    menu_atual = 'Principal'
    item_atual = 0
    while menu_atual != 'Sair' and game:
        menu = MENUS[menu_atual]
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                game = False

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    menu_atual = menu[item_atual]
                if event.key == pygame.K_UP:
                    item_atual -= 1
                    if item_atual < 0:
                        item_atual = 0
                if event.key == pygame.K_DOWN:
                    item_atual += 1
                    if item_atual >= len(menu):
                        item_atual = len(menu) - 1

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Desenha os textos na tela
        # Desenha o título do menu
        text_image = font.render(menu_atual, True, WHITE)
        screen.blit(text_image, (300, 10))
        for i in range(len(menu)):
            text = menu[i]
            if i == item_atual:
                text = '> ' + text
            else:
                text = '  ' + text
            text_image = font.render(text, True, WHITE)
            screen.blit(text_image, (100, 80 + (i + 1) * 16))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()








# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)



# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()