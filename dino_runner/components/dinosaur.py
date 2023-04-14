import pygame
import os

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, JUMP_VEL, X_POS, Y_POS, DEFAULT_TYPE, RUNNING_SHIELD, Y_POS_DUCK 


RUN_IMG = {DEFAULT_TYPE: RUNNING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING}
DUCK_IMG = {DEFAULT_TYPE: DUCKING}

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True 
        self.dino_jump = False # passei para false para resolver o bug do inicio, pq ele estava pulando
        self.dino_duck = False # criação do duck
        self.jump_vel = JUMP_VEL

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()        

        if user_input[pygame.K_UP] and not self.dino_jump: #adicionei dino duck as condições, para que não possam ocorrer em concomitancia
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True   

        if self.step_index >= 10:
            self.step_index = 0    

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5]  #seleciona a imagem e a alternancia para causar o efeito de movimento do dino
        
        self.dino_rect.y = Y_POS_DUCK #passagem da altura da imagem
        self.step_index+=1            #incremento do step index para alterar entres as imagens e causar o efeito de movimento do dino
        
        self.dino_duck = False        #o dino fica como falso para que quando a tecla pare de ser pressionada ele se levante sozinho 
     
