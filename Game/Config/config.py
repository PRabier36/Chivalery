
import pygame
import pygame_menu
from pygame_menu import Theme

HAUTEUR_FENETRE = 720
LARGEUR_FENETRE = 1080


background_img = './Game/Template/chivalry.jpg'

#
running = True
Version = "0.0.1-Alpha"
WinTitle = "Chivalry: Knight School {}".format(Version)
pygame.display.set_caption(WinTitle)
# BtnFont = pygame.font.SysFont('Harrington', 25)
screen = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
width = screen.get_width()
height = screen.get_height()
background = pygame.image.load('./Game/Template/chivalry.jpg')
# IMAGE_Chivalry_WALLPAPER = __images_path__.format('wallpaper.jpg')
font = pygame_menu.font.FONT_NEVIS

temptest = pygame_menu.baseimage.BaseImage(
    image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)

lowopacity = Theme(background_color=temptest,  # transparent background
                   title_font_color=(255, 255, 255),
                   title_font_shadow=True,
                   widget_padding=25,
                   widget_font=font)