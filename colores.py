import pygame, sys
import random
from pygame.locals import * #This imports constants like QUIT
import glob
import main as menu #Avoid conflict while calling main.py's main()

FPS = 60
SCREENWIDTH = 1280
SCREENHEIGHT = 720

def loadCat():
    imageLibrary = glob.glob('img/colores/stand*.png')
    cat = []
    for item in sorted(imageLibrary):
        cat.append(pygame.image.load(item))
        print item
    return cat


def cat(cat, posx, posy, status, surface):
    if status == "standing":
        for i in range(0,len(cat),1):
            surface.blit(cat[i], (posx, posy))
            pygame.display.flip()
            pygame.time.delay(100)
            print i



def loadSound():
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096) #pre init to avoid lag
    pygame.mixer.init()
    soundLibrary = glob.glob('sounds/colores/*.wav')
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

    interval = .04
    cycle = 0

    red = 0
    green = 0
    blue = 0
    i=0

    scalex = SCREENHEIGHT / 10

    close = pygame.image.load('img/close.png')
    scaledClose = pygame.transform.scale(close, (scalex, scalex))



    while True:
        milliseconds = fpsClock.tick(FPS) #ms since last frame
        seconds = milliseconds / 1000.0

        cycle += seconds


        if cycle > interval:
            surface.fill((red, green, blue))
            surface.blit(movingCat[i], (10, 10))
            surface.blit(scaledClose, (SCREENWIDTH - scalex - 50, SCREENHEIGHT - scalex - 50))

            i += 1

            if i >= len(movingCat):
                i=0
            cycle = 0



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == pygame.K_F1:
                pygame.mixer.quit()
                pygame.quit()
                menu.main()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print pos
                print scaledClose.get_offset()
                print scaledClose.collidepoint(pos)
                if scaledClose.collidepoint(pos):
                    pygame.mixer.quit()
                    pygame.quit()
                    menu.main()

            if event.type == KEYDOWN:
                red = random.randrange(0,255,1)
                green = random.randrange(0,255,1)
                blue = random.randrange(0,255,1)

                surface.fill((red, green, blue))
                surface.blit(movingCat[i], (10, 10))
                samples[(random.randrange(0,len(samples),1))].play() #Kind of spaguetti, but allows to add more sounds without toching the code




        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
