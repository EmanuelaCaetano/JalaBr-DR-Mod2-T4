from dino_runner.utils.constants import APPLE, DEFAULT_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Apple(PowerUp):
    def __init__(self):
        self.image = APPLE
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)
        