import pygame
from ..Config.config import *


class CustomButton:

    def __init__(self, colorCB, xCB, yCB, widthCB, heightCB, textCB=''):
        self.color = colorCB
        self.x = xCB
        self.y = yCB
        self.width = widthCB
        self.height = heightCB
        #self.cmd = cmd
        self.text = textCB

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Harrington', 24, bold=True)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def hover(self, button, pos):
        if button.isOver(pos):
            button.color = (202, 111, 30)
        else:
            button.color = (235, 152, 78)