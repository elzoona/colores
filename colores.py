import pygame, sys
import random
from pygame.locals import * #This imports constants like QUIT
import glob
import main as menu #Avoid conflict while calling main.py's main()

FPS = 30
SCREENWIDTH = 1280
SCREENHEIGHT = 720




def loadCat():
    imageLibrary = glob.glob('img/stand*.png')
    cat = []
    for item in imageLibrary:
        cat.append(pygame.image.load(item))
    return cat


def cat(cat, posx, posy, status, surface):
    if status == "standing":
        for i in range(0,len(cat),1):
            surface.blit(cat[i], (posx, posy))
            pygame.display.flip()
            pygame.time.delay(100)
            surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
            print i



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
    samples = loadSound()
    movingCat = loadCat()


    while True:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == pygame.K_F1:
                pygame.mixer.quit()
                pygame.quit()
                menu.main()

            if event.type == KEYDOWN:
                surface.fill((random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1)))
                samples[(random.randrange(0,len(samples),1))].play() #Kind of spaguetti, but allows to add more sounds without toching the code
                cat(movingCat, 10, 10, "standing", surface)


        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
