import pygame as pg

from entities.snake import Snake
from entities.food import Food
from systems.input_handler import InputHandler
from systems.collision import check_wall_collision, check_self_collision
from states.base_state import BaseState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state:BaseState = None

    def change_state(self, new_state):
        self.state = new_state

    def reset(self):
        pass

    def handle_events(self):
        pass

    def update(self):
        pass
    
    def draw(self, screen):
        pass