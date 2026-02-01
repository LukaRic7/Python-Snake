import pygame as pg

from entities.snake import Snake
from entities.food import Food
from systems.input_handler import handle_input
from systems.collision import check_wall_collision, check_self_collision

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = None

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