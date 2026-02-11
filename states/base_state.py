from abc import ABC, abstractmethod
import pygame as pg

# Used as an interface
class BaseState(ABC):
    def __init__(self, game): # Cannot set game type due to circular import err
        self.game = game

    @abstractmethod
    def handle_events(self, events:list[pg.event.Event]): pass

    @abstractmethod
    def update(self, delta_time:float): pass

    @abstractmethod
    def draw(self, screen:pg.Surface): pass