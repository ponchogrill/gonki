from random import randint
import pygame as pg
import sys
FPS = 60
W = 800
H = 1000
WHITE = (255, 255, 255)
class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center = (x, 0))
        self.surf = pg.image.load('car1.png').convert()
        scale = pg.transform.scale(self.surf, (self.surf.get_width() // 4,
               self.surf.get_height() // 4))
    def update(self):
        keys = pygame.key.get_pressed()
        #если нажата
        if keys[pygame.K_d]:
            self.speed_x = 10
        #если нажата
        if keys[pygame.K_a]:
            self.speed_x = -10
        self.x += self.speed_x
        self.speed_x = 0

 
sc = pg.display.set_mode((W, H))
clock = pg.time.Clock() 
# координата x будет случайна
car1 = Car(randint(1, W), 'car1.png')
grass = Car(randint(1, W), 'grass.png')
 
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
 
    sc.fill(WHITE)
    sc.blit(grass.image, grass. rect)
    sc.blit(car1.image, car1.rect)
    pg.display.update()
