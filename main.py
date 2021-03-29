# main du projet Chivalery
import pygame
import pygame_menu
import config

pygame.init()
running = True
Version = "0.0.1-Alpha"
WinTitle = "Chivalry: Knight School {}".format(Version)
system_Font = pygame.font.SysFont("Harrington", 40)

font = pygame_menu.font.FONT_NEVIS

surface = pygame.display.set_mode((1080, 720))
background = pygame.image.load('./Game/Template/chivalry.jpg')

class Main:

    def set_difficulty(value, difficulty):
        # Do the job here !
        pass

    def start_the_game():
        # Do the job here !
        pass

    menu = pygame_menu.Menu( 500, 300, 'Welcome',theme=pygame_menu.themes.THEME_BLUE)




    menu.add.button('Play', start_the_game)
    menu.add.button('Setting', start_the_game)
    menu.add.button('credits', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)
