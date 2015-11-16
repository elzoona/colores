import pygame, sys
import random
from pygame.locals import * #Esto importa las constantes

pygame.init()
surface = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Colores')
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
            pygame.mixer.Sound("sounds/"+str(random.randrange(1,66,1))+".wav").play()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.quit()

        pygame.display.update()
