from dino_runner.utils.constants import LIFE, DEFAULT_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Life(PowerUp):
    def __init__(self):
        self.image = LIFE
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)