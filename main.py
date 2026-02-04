import loggerric as lr
import pygame as pg

from game import Game
from states.main_menu import MainMenu
from utils.settings import Settings

def main():
    pg.init()

    lr.Log.info('Initializing...')

    screen = pg.display.set_mode(tuple(Settings.get('window').values()))
    pg.display.set_caption('Snake Game')

    clock = pg.time.Clock()

    game = Game(screen)
    game.change_state(MainMenu(game))

    FPS = Settings.get('game', 'fps')

    lr.Log.info('Entering Game Loop...')
    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        
        game.state.handle_events(events)
        game.state.update(dt)
        game.state.draw(screen)

        pg.display.flip()

    pg.quit()

if __name__ == '__main__':
    main()