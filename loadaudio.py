import pygame
import random
import glob

class LoadSound ():
    """Loads the directory where the sound files are

    Attributes:
        soundLibrary: relative path to files. Wildcars are allowed
    """
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096) #pre init to avoid lag
    pygame.mixer.init()

    def __init__(self, soundLibrary):
        self.soundLibrary = soundLibrary
        self.soundLibrary = glob.glob(self.soundLibrary)

    def create_list(self):
        samples = []
        for item in self.soundLibrary:
            samples.append(pygame.mixer.Sound(item))
        return samples

class LoadSprites ():
