import pygame
import os
pygame.init()

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

WIN_WIDTH = 900
WIN_HEIGHT = 600
FPS = 40

fon = pygame.image.load(file_path(r"images\35.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))
        
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speedx, speedy):
        super().__init__(x, y, width, height, image)
        self.speedx = speedx
        self.speedy = speedy
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image,True, False)


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy




player = Player(100, 50, 50, 50, r"images\35.png", 0, 0)
enemy = GameSprite(40,420,55,40, r"images\33.jpg")
finish = GameSprite(390, 39, 50, 50, r"images\34.png")

walls = pygame.sprite.Group()
wall1 = GameSprite(20, 30, 300, 90, r"images\35.png")
walls.add(wall1)


#walls.add(wall2)

levl = 1
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if levl == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.speedx = 4
                    player.direction = "right"
                    player.image = player.image_r  
                if event.key == pygame.K_a:              
                    player.speedx = -4
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_w:
                    player.speedy = -4
                if event.key == pygame.K_s:
                    player.speedy = 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.speedx = 0
                if event.key == pygame.K_a:
                    player.speedx == 0
                if event.key == pygame.K_w:
                    player.speedy = 0
                if event.key == pygame.K_s:
                    player.speedy = 0   


    if levl == 1:
       window.blit(fon, (0, 0))
       player.show()
       player.update()
       enemy.show()
       finish.show()
       walls.draw(window)

    clock.tick(FPS)
    pygame.display.update()



