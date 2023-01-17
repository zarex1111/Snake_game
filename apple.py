import pygame
from pygame.sprite import Sprite

from random import randrange

class Apple(Sprite):
    def __init__(self, game):
        super().__init__()
        
        self.screen = game.screen
        self.game = game
        self.settings = game.settings
        
        self.image = pygame.image.load('images/APPLE.bmp')
        self.rect = self.image.get_rect()
        
        x = randrange(0, self.settings.width, 40)
        y = randrange(0, self.settings.height, 40)
        self.rect.x = x
        self.rect.y = y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)