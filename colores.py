import pygame, sys
import random
from pygame.locals import * #This imports constants like QUIT
pygame.init()
surface = pygame.display.set_mode((1280,720), 1, 32)
pygame.display.set_caption('Colores')
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096) #Check for better values

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.quit()
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
            pygame.mixer.Sound("sounds/"+str(random.randrange(1,66,1))+".wav").play() #FIXME some latency problems


        pygame.display.update()
