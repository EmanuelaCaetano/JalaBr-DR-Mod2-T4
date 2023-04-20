import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.snow import Snow

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        Obstacle_type = [
            Cactus(),
            Bird(),
            Snow()
        ]    
        if len(self.obstacles) == 0:
            self.obstacles.append(Obstacle_type[random.randint(0,2)])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count -= 1
                    break

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
