# ===== Inicialização =====
# ----- Importa e inicia pacotes---


import pygame

# ----- Gera tela principal

WIDTH = 700
HEIGHT = 400
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Inicia pygame e cria uma janela(tela)
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WANDA E VISION")
clock = pygame.time.Clock()

# ----- Inicia assets

tela_principal= os.path.join('imagens', 'background_principal.jpg')
background1 = os.path.join('imagens', 'Imagem1.png')
feiticeira_image = os.path.join('imagens','wanda.png')


#-----------carregando imagens

startscreen=pygame.image.load(tela_principal)
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))
background = pygame.image.load(background1)
feiticeira_image = pygame.image.load(feiticeira_image).convert_alpha()

##Escreve na Tela
font_name = pygame.font.match_font('arial') #fonte da letra

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmob(): #adicionar helicopetero no all_sprites
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    mobs.add(m)


#funcão para o status bar
def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


class Feiticeira(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(feiticeira_image,(80,60))#reajuste de tamanho das imagens
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/10
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
        self.shield = 100 #"status bar"-
         # Só será possível atirar uma vez a cada 500 milissegundos

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def shoot(self, mx, my):
        bullet = Bullet(self.rect.topleft,self.rect.top, mx, my)
        all_sprites.add(bullet)
        bullets.add(bullet)
        flecha_sound.play()


class Mob(pygame.sprite.Sprite):  # classe dos helicopetros do exercito
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(dragao_image, (60, 35))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(HEIGHT - self.rect.height)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-2, 2)
        self.rot = 0  # para os dragoes rotacionarem
        self.rot_speed = random.randrange(-8, 8)  # velocida de rotacao
        self_last_update = pygame.time.get_ticks()


class Bullet(pygame.sprite.Sprite):  # classe para poderes da wanda
    def __init__(self, x, y, mx, my):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(flecha_image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.topleft = x
        self.speedy = my - arqueiro.rect.top
        self.speedx = mx - arqueiro.rect.centerx

        self.lad_x = mx - arqueiro.rect.centerx  # lado x e lado y para calcular o pitagoras
        self.lad_y = my - arqueiro.rect.centery
        self.tang = self.lad_y / self.lad_x
        if self.lad_x == 0 and self.lad_y > 0:
            self.angle = 360 - 90
        elif self.lad_x == 0 and self.lad_y < 0:
            self.angle = 360 - 180
        else:
            if self.lad_x > 0 and self.lad_y < 0:
                self.angle = - math.degrees(math.atan(self.tang))
            elif self.lad_x > 0 and self.lad_y > 0:
                self.angle = 360 - math.degrees(math.atan(self.tang))
            elif self.lad_x < 0 and self.lad_y > 0:
                self.angle = 180 - math.degrees(math.atan(self.tang))
            elif self.lad_x < 0 and self.lad_y < 0:
                self.angle = 180 - math.degrees(math.atan(self.tang))
