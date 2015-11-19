import pygame
import colores

def read():
    print '1 - Colores'
    game = raw_input('From this beautiful menu, select the game: ')
    return game

def main():
    game=read()
    while game !='q':
        if game == '1':
            colores.main()
        else:
            game=read()
    quit()


if __name__ == '__main__':
    main()
