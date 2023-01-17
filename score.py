import pygame.font

class Score:
    
    def __init__(self, game, msg, n):
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.width, self.height = 75, 75
        
        self.text_color = (25, 35, 0)
        self.font = pygame.font.SysFont(None, 20)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right - 100 * n
        
        self._prep_msg(msg)    
        
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)     