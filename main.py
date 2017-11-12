import colores
import loadassets
import pygame

def read():
    print ('1 - Colores')
    game = input('From this beautiful menu, select the game: ')
    return game

def main():
    game=read()
    print (game)
    while game !='q':
        if game == '1':
            colores.main()
        else:
            game=read()
    quit()


if __name__ == '__main__':
    main()
