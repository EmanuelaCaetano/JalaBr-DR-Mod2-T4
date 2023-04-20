import random
import pygame

from dino_runner.utils.constants import APPLE
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.apple import Apple
from dino_runner.components.powerups.life import Life
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components import game


class PowerUpManager:
    
    def __init__(self, game):
        self.apples = 0
        self.power_ups = []
        self.when_appears = 0
        self.game = game

    def generate_power_ups(self, score): 
        power_up_types = [Shield(), Apple(), Life()]
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(power_up_types[random.randint(0,2)])
            #power_up_type = random.choice(power_up_types) self.obstacles.append(Obstacle_type[random.randint(0,2)])
            #self.power_ups.append(power_up_type)          

    def update(self, score, game_speed, player):
        self.generate_power_ups(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect) and isinstance(power_up, Shield):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
            elif player.dino_rect.colliderect(power_up.rect) and isinstance(power_up, Apple):
                player.type = power_up.type
                self.power_ups.remove(power_up)
    
                self.apples += 1
                if self.apples % 3 == 0:
                    self.game.death_count += 1
            elif player.dino_rect.colliderect(power_up.rect) and isinstance(power_up, Life):
                self.game.death_count += 1

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        screen.blit(APPLE, (20, 70))
        draw_message_component(
            f"{self.apples}",
            screen,
            pos_x_center=70,
            pos_y_center=85
        )

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)

# import random
# import pygame

# from dino_runner.components.powerups.shield import Shield


# class PowerUpManager:
    
#     def __init__(self):
#         self.power_ups = []
#         self.when_appears = 0

#     def generate_power_ups(self, score):
#         if len(self.power_ups) == 0 and self.when_appears == score:
#             self.when_appears += random.randint(200, 300)
#             self.power_ups.append(Shield())           

#     def update(self, score, game_speed, player):
#         self.generate_power_ups(score)
#         for power_up in self.power_ups:
#             power_up.update(game_speed, self.power_ups)
#             if player.dino_rect.colliderect(power_up.rect):
#                 power_up.start_time = pygame.time.get_ticks()
#                 player.shield = True
#                 player.has_power_up = True
#                 player.type = power_up.type
#                 player.power_up_time = power_up.start_time + (power_up.duration * 1000)
#                 self.power_ups.remove(power_up)

#     def draw(self, screen):
#         for power_up in self.power_ups:
#             power_up.draw(screen)

#     def reset_power_ups(self):
#         self.power_ups = []
#         self.when_appears = random.randint(200,300)