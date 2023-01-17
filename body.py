import pygame
from pygame.sprite import Sprite

class Body(Sprite):
    def __init__(self, game, bodies, head):
        super().__init__()
        
        self.screen = game.screen
        self.game = game
        self.settings = game.settings

        if len(bodies) > 0:
            self.next_body = bodies.sprites()[-1]
        else:
            self.next_body = head
            
        self._set_direction(self.next_body)
        if self.direction_x != 0:
            self.image = pygame.image.load('images/body_horizontal.bmp')
        else:
            self.image = pygame.image.load('images/body_vertikal.bmp')
        self.rect = self.image.get_rect()
        
        self._set_rect(self.next_body)
        
        
    
    def update(self):    
        self._move()
        self._change()
               
    def _move(self):
        self.y = float(self.rect.y)
        self.y += self.settings.snake_speed * self.direction_y
        self.rect.y = self.y
        
        self.x = float(self.rect.x)
        self.x += self.settings.snake_speed * self.direction_x
        self.rect.x = self.x       
        
    def _change(self):
        if self.next_body.direction_x != self.direction_x:
            self.direction_x = self.next_body.direction_x
            
            if self.direction_x != 0:
                self.image = pygame.image.load('images/body_horizontal.bmp')
            else:
                self.image = pygame.image.load('images/body_vertikal.bmp')
            self.rect = self.image.get_rect()
            
            self.rect.y = self.next_body.rect.y
            self.rect.x = self.next_body.rect.x
            
        if self.next_body.direction_y != self.direction_y:
            self.direction_y = self.next_body.direction_y 
            
            if self.direction_x != 0:
                self.image = pygame.image.load('images/body_horizontal.bmp')
            else:
                self.image = pygame.image.load('images/body_vertikal.bmp')            
            self.rect = self.image.get_rect()
            
            self.rect.x = self.next_body.rect.x
            self.rect.y = self.next_body.rect.y           
            
        
    def _set_rect(self, body):
        x1 = self.direction_x
        x2 = body.direction_x
        y1 = self.direction_y
        y2 = body.direction_y
        if y1 == y2 == -1:
            self.rect.top = body.rect.bottom + 40
            self.rect.left = body.rect.left
        elif y1 == y2 == 1:
            self.rect.bottom = body.rect.top - 40
            self.rect.left = body.rect.left
        elif x1 == x2 == 1:
            self.rect.x = body.rect.x - 40
            self.rect.y = body.rect.y
        elif x1 == x2 == -1:
            self.rect.left = body.rect.right + 40
            self.rect.bottom = body.rect.bottom
            
    def _set_direction(self, body):
        self.direction_x = body.direction_x
        self.direction_y = body.direction_y        