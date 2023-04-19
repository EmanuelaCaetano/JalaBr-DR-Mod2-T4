import pygame
import os

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, X_POS_BG, Y_POS_BG, GAME_SPEED, DEFAULT_TYPE, TRY, FIRST, BOOM, OVER, HART
from dino_runner.utils.text_utils import draw_message_component

from dino_runner.components.dinosaur import Dinosaur 
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        #Score
        self.running = False

        self.game_speed = GAME_SPEED
        self.x_pos_bg = X_POS_BG
        self.y_pos_bg = Y_POS_BG
        self.death_count = 3
        #score
        self.score = 0
        self.best_score = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        

    #score
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()   

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.game_speed = GAME_SPEED
        #score
        self.score = 0

        while self.playing:
            self.events()
            self.update()
            self.draw()
        #Score, removo o quit()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False 
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        #score
        self.update_score()
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        #score
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    #score
    def draw_score(self):
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
        )
        if self.score > self.best_score:
            self.best_score = self.score

        draw_message_component(
            f"Best Score: {self.best_score}",
            self.screen,
            pos_x_center=100,
            pos_y_center=50
        )

        self.x = -200       
        for i in range(self.death_count):
            self.screen.blit(HART, (self.x + (50 * i), -150))
            


    #adicionar harts

    #score
    def handle_events_on_menu(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run() 
    #score            
    def show_menu(self):
        self.start_count = 1 #variavel para começar, para não ocorrer erro de logica
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 3 and self.start_count == 1:
            draw_message_component("Press any key to start", self.screen, pos_y_center=half_screen_height + 250)
            self.screen.blit(FIRST, (half_screen_width - 270, half_screen_height - 300))
            self.start_count -= 1
        elif self.death_count > 0:
            draw_message_component("Press any key to continue to play", self.screen, pos_y_center=half_screen_height + 140)
            draw_message_component(
                f"Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )          
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(TRY, (half_screen_width -200, half_screen_height - 80))
            
        elif self.death_count == 0:
            self.screen.blit(BOOM, (half_screen_width - 270, half_screen_height - 300))
            self.screen.blit(OVER, (350, half_screen_height + 200 ))
            pygame.time.delay(1000)
            pygame.QUIT
            
        pygame.display.update() 
        self.handle_events_on_menu()



# import pygame

# from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, X_POS_BG, Y_POS_BG, GAME_SPEED
# from dino_runner.components.dinosaur import Dinosaur
# from dino_runner.components.obstacles.obstacle_manager import ObstacleManager 


# class Game:
#     def __init__(self):
#         pygame.init()
#         pygame.display.set_caption(TITLE)
#         pygame.display.set_icon(ICON)
#         self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         self.clock = pygame.time.Clock()
#         self.playing = False
#         self.game_speed = GAME_SPEED
#         self.x_pos_bg = X_POS_BG
#         self.y_pos_bg = Y_POS_BG

#         self.player = Dinosaur()
#         self.obstacle_manager = ObstacleManager()
#         self.death_count = 0

#     def run(self):
#         # Game loop: events - update - draw
#         self.playing = True
#         while self.playing:
#             self.events()
#             self.update()
#             self.draw()
#         pygame.quit()

#     def events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.playing = False
#                 self.running = False

#     def update(self):
#         user_input = pygame.key.get_pressed()
#         self.player.update(user_input)
#         self.obstacle_manager.update(self)

#     def draw(self):
#         self.clock.tick(FPS)
#         self.screen.fill((255, 255, 255))
#         self.draw_background()
#         self.player.draw(self.screen)
#         self.obstacle_manager.draw(self.screen) #desenho ds obstaculos no jogo
#         pygame.display.update()
#         pygame.display.flip()

        
#     def draw_background(self):
#         image_width = BG.get_width()
#         self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
#         self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
#         if self.x_pos_bg <= -image_width:
#             self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
#             self.x_pos_bg = 0
#         self.x_pos_bg -= self.game_speed
