import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from utils.settings import Settings
from ui.background import Grid
from game import Game
from entities.snake import Snake
from entities.food import Food
from systems.input_handler import InputHandler
from systems.collision import check_wall_collision, check_self_collision
from utils.sound import AudioManager

class PlayState(BaseState):
    """
    **Play state menu state.**
    
    Handles the play state menu screen.
    """

    def __init__(self, game:Game, username:str):
        """
        **Initialization.**
        
        *Parameters*:
        - `game` (Game): The game to tie the class too.
        """

        super().__init__(game)

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.window_size = Settings.get('window_size')

        self.luka_sfx = Settings.get('game', 'luka_sfx')

        # Init plain background class
        self.background = Grid(cell_size=40)

        self.username = username

        # Game entities
        self.snake = Snake()
        self.foods:list[Food] = []
        for _ in range(Settings.get('game', 'num_apples')):
            food = Food(
                self.window_size['width'], self.window_size['height'], 40
            )
            self.foods.append(food)
            food.respawn(self.snake.body)  # Dont spawn inside the snake
        
        self.input_handler = InputHandler()

        # Timers for controlled update speed
        self.snake_update_timer = 0
        self.snake_update_interval = 1 / Settings.get('game', 'snake_fps')

        # Score
        self.score = 0

        lr.Log.debug(f'Play state initialized, playing as: {username}')

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for event in events:
            self.input_handler.handle_event(event, self.snake)

    def update(self, delta_time:float):
        self.snake_update_timer += delta_time
        if self.snake_update_timer >= self.snake_update_interval:
            self.snake_update_timer -= self.snake_update_interval

            # Get next direction from input handler
            new_dir = self.input_handler.get_next_direction(self.snake.direction)
            self.snake.set_direction(new_dir)

            # Move snake
            self.snake.move()

            # Check collisions
            if (check_wall_collision(self.snake.head())
                or check_self_collision(self.snake.body)):
                if self.luka_sfx:
                    AudioManager.play('luka_death.mp3', 'sfx')
                else:
                    AudioManager.play('death.mp3', 'sfx')

                # Game over - switch to death menu
                from states.death_menu import DeathMenu
                self.game.change_state(DeathMenu(
                    self.game, self.username, self.score
                ))
                return

            # Check food collision
            for food in self.foods:
                if self.snake.head() == food.position:
                    if self.luka_sfx:
                        AudioManager.play('luka_eat.mp3', 'sfx')
                    else:
                        AudioManager.play('eat.mp3', 'sfx')
                    self.snake.grow()
                    food.respawn(self.snake.body)
                    self.score += 1
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Draw entities
        self.snake.draw(screen, self.colors['primary_accent'])

        for food in self.foods:
            food.draw(screen, self.colors['red'])