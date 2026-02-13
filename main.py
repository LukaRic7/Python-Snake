import loggerric as lr
import pygame as pg
import traceback

from states.main_menu import MainMenu
from utils.sound import AudioManager
from utils.settings import Settings
from game import Game

def main():
    """**Main entry point.**"""

    pg.init()

    lr.Log.info('Initializing...')

    # Create window
    screen = pg.display.set_mode(tuple(Settings.get('window_size').values()))
    pg.display.set_caption('Snake Game')

    # Init clock
    clock = pg.time.Clock()

    # Set the default game state (main menu)
    game = Game(screen)
    game.change_state(MainMenu(game))

    FPS = Settings.get('game', 'fps')

    # Start bg music
    AudioManager.play('background_music.mp3', 'music', loops=-1)

    # Mainloop
    lr.Log.info('Entering Game Loop...')
    
    try:
        running = True
        while running:
            # Grab delta time
            dt = clock.tick(FPS) / 1000

            # Grab events this frame
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
            
            # Call current state methods
            game.state.handle_events(events)
            game.state.update(dt)
            game.state.draw(screen)

            pg.display.flip()
    except Exception as e:
        lr.Log.error('Unhandled error occured during runtime:', e)
        traceback.print_exc() # Prints entire callstack up until error
    finally:
        pg.quit()

if __name__ == '__main__':
    main()