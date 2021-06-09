# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 400 # Altura da tela
FPS = 60 # Frames por segundo

#------cores-----------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Inicialização do Pygame e criajanela
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WANDA E VISION")
clock = pygame.time.Clock()




# ----- Inicia assets-----------
background1 = pygame.image.load('imagens/background_principal.jpg')
background1=pygame.transform.scale(background1, (WIDTH,HEIGHT))
background2 = pygame.image.load('imagens/background_familia.jpg')
background2=pygame.transform.scale(background2, (WIDTH,HEIGHT))
#----Carregando imagens-----------







#----------MENU E TELA PRINCIPAL-------

# Define a sequência de textos do menu
MENUS = {
    'Principal': ['Proteja Wanda e sua Família', 'Duelo', 'Sair'],
    'Proteja Wanda e sua Família': [
        'Wanda criou uma dimensão alternativa para viver em paz com sua família,',
        'no entanto, ela foi descoberta pelas forças armadas.',
        'Agora ela para proteger sua famíla terá que destruir todas as tropas,',
        'ajude Wanda a aniquilar o máximo de tropas que você puder e mantenha ela e sua família segura!'
    ],
    'Duelo': ['Você ja esta pronto para duelar!! Agora mostre do que você é capaz.',],
    'Sair': [''],
}



def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega a fonte padrão do sistema
    font = pygame.font.SysFont(None, 16)

    # controla o texto a ser mostrado
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
#---------------------------------------------

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Desenha os textos na tela
        # Desenha o título do menu
        text_image = font.render(menu_atual, True, WHITE)
        screen.blit(background1, (0, 0))


        for i in range(len(menu)):
            text = menu[i]
            if i == item_atual:
                text = '> ' + text
            else:
                text = '  ' + text
            text_image = font.render(text, True, WHITE)
            screen.blit(text_image, (150, 80 + (i +0.2) * 30))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()



# evita travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()