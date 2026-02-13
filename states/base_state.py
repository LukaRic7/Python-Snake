from abc import ABC, abstractmethod
import pygame as pg

# Used as an interface
class BaseState(ABC):
    """
    **BaseState for game states classes.**
    
    Used as an interface.
    """

    def __init__(self, game): # Cannot set game type due to circular import err
        """
        **Initialization.**
        
        *Parameters*:
        - `game` (Game): The game to tie the class to.
        """
        
        self.game = game

    @abstractmethod
    def handle_events(self, events:list[pg.event.Event]):
        """
        **Handles pygame events**
        
        *Parameters*:
        - `events` (list[pg.event.Event]): List of pygame events made this frame.
        """
        
        pass

    @abstractmethod
    def update(self, delta_time:float):
        """
        **Handles variable updates during runtime.**
        
        *Parameters*:
        - `delta_time` (float): Delta time for this and the last frame.
        """

        pass

    @abstractmethod
    def draw(self, screen:pg.Surface):
        """
        **Handles drawing on every frame.**
        
        *Parameters*:
        - `screen` (pg.Surface): Surface screen to draw on.
        """
        
        pass