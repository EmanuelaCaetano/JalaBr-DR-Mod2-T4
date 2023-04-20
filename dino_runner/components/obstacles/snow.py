from dino_runner.utils.constants import SNOW
from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Snow(Obstacle):
    def __init__(self):
        super().__init__(SNOW, 0)
        self.rect.y = self.y_pos_cloud =  random.randint(0, 270)
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0