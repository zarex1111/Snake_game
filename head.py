import pygame

class Head():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/HEAD_RIGHT.bmp')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left - 20
        self.rect.left = 120
        
        self.settings = game.settings
        
        self.direction_y = 0
        self.direction_x = 1
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if (self.direction_y == 0 and self.rect.right <= self.screen_rect.right and
                self.rect.left >= 0):
            self.x = float(self.rect.x)
            self.x += self.settings.snake_speed * self.direction_x
            self.rect.x = self.x
        
        elif (self.direction_x == 0 and self.rect.bottom <= self.screen_rect.bottom and
                self.rect.top >= 0):
            self.y = float(self.rect.y)
            self.y += self.settings.snake_speed * self.direction_y
            self.rect.y = self.y
            
    def change_direction(self, x, y, bottom, right):
        self.direction_x = x
        self.direction_y = y
        
        if x == 1:
            last = self.rect
            self.image = pygame.image.load('images/HEAD_RIGHT.bmp')
            self.rect = self.image.get_rect()
            
            self.rect = last
        if x == -1:
            last = self.rect
            self.image = pygame.image.load('images/HEAD_LEFT.bmp')
            self.rect = self.image.get_rect()
            
            self.rect = last

        if y == -1:
            last = self.rect
            self.image = pygame.image.load('images/HEAD_UP.bmp')
            self.rect = self.image.get_rect()
            self.rect = last
        if y == 1:
            last = self.rect
            self.image = pygame.image.load('images/HEAD_DOWN.bmp')
            self.rect = self.image.get_rect()
            self.rect = last