import pygame
import os
import json

from time import sleep

from settings import Settings

from head import Head

from body import Body

from apple import Apple

from stats import Stats

from buttons import Button

from score import Score

from speed_button import Speed_Button


class Snake:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,
                                               self.settings.height))
        pygame.display.set_caption('ЗМЕЙКА')
        
        self.head = Head(self)
        
        self.bodies = pygame.sprite.Group()
        for _ in range(0):
            body = Body(self, self.bodies, self.head)
            self.bodies.add(body)            
        self.screen_rect = self.screen.get_rect()
        
        self.apple = Apple(self)
        while pygame.sprite.spritecollideany(self.apple, self.bodies):
            self.apple = Apple(self)
        self.apples = pygame.sprite.Group()
        self.apples.add(self.apple)
        
        self.stats = Stats()
        
        self.play_button = Button(self, 'PLAY')
        
        self.score = Score(self, f'Score: {str(int(self.stats.score))}', 1)
        
        with open('data/best_score.json') as f:
            self.best_score = json.load(f)
        self.best_score_button = Score(self, f'Best score: {self.best_score}', 2)
        
        self.speed_buttons = []
        new_button = Speed_Button(self, 'Noob mode', -2, 0.2)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Normal mode', -1, 0.1)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Hard mode', 1, 0.05)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Impossible mode', 2, 0.035)
        self.speed_buttons.append(new_button)        
        
    def run_game(self):
        while True:
            self._check_head_body()
            self._check_head_walls()
            
            if not (self.stats.button_clicked):
                self._check_events()
                self._update_screen()
            
            elif not self.stats.speed_choosed:
                self._check_events()
                self._update_screen()
                
            elif self.stats.game_is_active:
                self._check_events()
                
                self._update_bodies()
                
                self.head.update()
                
                self._check_apple()
            
                self._update_screen()
            
                sleep(self.settings.snake_time)
            else:
                if self.stats.score > self.stats.best_score:
                    with open('data/best_score.json', 'w') as f:
                        json.dump(int(self.stats.score), f)
                self.new_game()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)  
            elif event.type == pygame.KEYDOWN:
                left = self.head.rect.right
                right = self.head.rect.bottom
                if event.key == pygame.K_s and self.head.direction_y == 0:
                    self.head.change_direction(0, 1, left, right)
                if event.key == pygame.K_w and self.head.direction_y == 0:
                    self.head.change_direction(0, -1, left, right)
                if event.key == pygame.K_d and self.head.direction_x == 0:
                    self.head.change_direction(1, 0, left, right)
                if event.key == pygame.K_a and self.head.direction_x == 0:
                    self.head.change_direction(-1, 0, left, right)
                    
                if event.key == pygame.K_q:
                    os._exit(0)
                
                if event.key == pygame.K_p:
                    sleep(100)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_speed_buttons(mouse_pos)
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.head.blitme()
        self.apple.blitme()
        self.bodies.draw(self.screen)
        
        self.score = Score(self, f'Score: {str(int(self.stats.score))}', 1)
        self.score.draw_button()
        
        self.best_score_button.draw_button()
        
        if not self.stats.button_clicked:
            self.play_button.draw_button()
            
        elif not self.stats.speed_choosed:
            for button in self.speed_buttons:
                button.draw_button()
                
        if self.stats.speed_choosed and self.stats.button_clicked:
            self.stats.game_is_active = True
        
        pygame.display.flip()
    
    def _update_bodies(self):
        for body in self.bodies.sprites()[::-1]:
            body.update()
    
    def _check_head_walls(self):
        if not (self.head.rect.right <= self.screen_rect.right and self.head.rect.left >= 0 and
                self.head.rect.bottom <= self.screen_rect.bottom and self.head.rect.top >= 0):
            self.stats.game_is_active = False
    
    def _check_head_body(self):
        if pygame.sprite.spritecollideany(self.head, self.bodies):
            self.stats.game_is_active = False
    
    def _check_apple(self):
        if pygame.sprite.spritecollideany(self.head, self.apples):
            self.stats.score += 1 / self.settings.snake_time
            
            self.apples.empty()
            self.apple = Apple(self)
            while pygame.sprite.spritecollideany(self.apple, self.bodies):
                self.apple = Apple(self)            
            self.apples.add(self.apple)
            
            new_body = Body(self, self.bodies, self.head)
            self.bodies.add(new_body)
            
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            
            self.stats.button_clicked = True
            
    def _check_speed_buttons(self, mouse_pos):
        for button in self.speed_buttons:
            if button.rect.collidepoint(mouse_pos):
                self.stats.speed_choosed = True
                self.settings.snake_time = button.snake_time
                
    def new_game(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,
                                               self.settings.height))
        pygame.display.set_caption('ЗМЕЙКА')
        
        self.head = Head(self)
        
        self.bodies = pygame.sprite.Group()
        for _ in range(0):
            body = Body(self, self.bodies, self.head)
            self.bodies.add(body)            
        self.screen_rect = self.screen.get_rect()
        
        self.apple = Apple(self)
        while pygame.sprite.spritecollideany(self.apple, self.bodies):
            self.apple = Apple(self)
        self.apples = pygame.sprite.Group()
        self.apples.add(self.apple)
        
        self.stats = Stats()
        
        self.play_button = Button(self, 'PLAY')
        
        self.score = Score(self, f'Score: {str(int(self.stats.score))}', 1)
        
        with open('data/best_score.json') as f:
            self.best_score = json.load(f)
        self.best_score_button = Score(self, f'Best score: {self.best_score}', 2)
        
        self.speed_buttons = []
        new_button = Speed_Button(self, 'Noob mode', -2, 0.2)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Normal mode', -1, 0.1)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Hard mode', 1, 0.05)
        self.speed_buttons.append(new_button)
        new_button = Speed_Button(self, 'Impossible mode', 2, 0.035)
        self.speed_buttons.append(new_button)        
                
                    
if __name__ == '__main__':
    ai_game = Snake()
    ai_game.run_game()