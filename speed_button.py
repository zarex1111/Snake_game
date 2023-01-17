import pygame.font

class Speed_Button:
    
    def __init__(self, game, msg, n, snake_time):
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.width, self.height = self.screen_rect.width // 12, self.screen_rect.height // 16
        
        self.text_color = (25, 35, 0)
        self.button_color = (199, 199, 255)
        self.font = pygame.font.SysFont(None, self.screen_rect.width // 40)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        '''self.rect.right = self.screen_rect.right // 2 + 50 * n
        self.rect.top = self.screen_rect.top // 2 - 200'''
        self.rect.right = self.screen_rect.right // 2 + (self.screen_rect.width // 8) * n
        self.rect.bottom = self.screen_rect.bottom // 2
        
        self.snake_time = snake_time
        
        self._prep_msg(msg)    
        
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)  