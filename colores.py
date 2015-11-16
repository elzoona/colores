import pygame, sys
import random
from pygame.locals import * #This imports constants like QUIT
import glob

FPS = 30
SCREENWIDTH = 1280
SCREENHEIGHT = 720






cat = pygame.image.load('img/stand01.png')
catX=10
catY=10



def loadSound():
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096) #pre init to avoid lag
    pygame.mixer.init()
    soundLibrary = glob.glob('sounds/*.wav')
    samples = []
    for item in soundLibrary:
        samples.append(pygame.mixer.Sound(item))
    return samples



def main():
    global fpsClock, surface

    pygame.init()
    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 1, 32)

    pygame.display.set_caption('Colores')
    samples=loadSound()


    while True:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
                surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
                samples[(random.randrange(0,len(samples),1))].play() #Kind of spaguetti, but allows to add more sounds without toching the code
                surface.blit(cat, (catX, catY))

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
