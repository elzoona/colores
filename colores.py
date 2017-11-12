import pygame
import random
import loadassets
from pygame.locals import *

import main as menu

FPS=60
SCREENWIDTH=1280
SCREENHEIGHT=800

def moving_cat(cat, posx, posy, status, surface):
    if status == "standing":
        surface.blit(cat, (posx, posy))
        pygame.display.flip()
        pygame.time.delay(100)

def main():
    global fpsClock

    pygame.init()

    fpsClock = pygame.time.Clock()
    surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 1, 32)

    cat=loadassets.LoadSprites('img/colores/*.png').create_list()
    kalimba=loadassets.LoadSound('sounds/colores/*.wav').create_list()

    interval = .04
    cycle = 0

    red = 0
    green = 0
    blue = 0
    i=0

    while True:
        milliseconds = fpsClock.tick(FPS) #ms since last frame
        seconds = milliseconds / 1000.0

        cycle += seconds

        print "cycle: ", cycle
        print "interval: ", interval


        if cycle > interval:
            surface.fill((red, green, blue))
            moving_cat(cat[i], 10, 10, 'standing', surface)

            i += 1


            if i >= len(cat):
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

            """if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print pos
                print scaledClose.get_offset()
                print scaledClose.collidepoint(pos)
                if scaledClose.collidepoint(pos):
                    pygame.mixer.quit()
                    pygame.quit()
                    menu.main()"""

            if event.type == KEYDOWN:
                red = random.randrange(0,255,1)
                green = random.randrange(0,255,1)
                blue = random.randrange(0,255,1)

                surface.fill((red, green, blue))
                moving_cat(cat, 10, 10, 'staninf', surface)
                kalimba[(random.randrange(0,len(kalimba),1))].play() #Kind of spaguetti, but allows to add more sounds without toching the code




        pygame.display.update()
        pygame.display.flip()

if __name__ == '__main__':
    main()