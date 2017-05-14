import pygame
import sys
import main as menu

from pygame.locals import *

FPS = 60

SCREENWIDTH = 1280
SCREENHEIGHT = 720

def loadSound():
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096) #pre init to avoid lag
    pygame.mixer.init()
    soundLibrary = glob.glob('sounds/maracas/*.wav')
    samples = []
    for item in soundLibrary:
        samples.append(pygame.mixer.Sound(item))
    return samples
