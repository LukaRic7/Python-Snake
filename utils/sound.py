from pathlib import Path
import loggerric as lr
import pygame as pg

from utils.settings import Settings

class AudioManager:
    pg.mixer.init()
    pg.mixer.set_num_channels(16) # Concurrent

    # Group channels (via pygame, same channel sounds)
    channels = { 'music': pg.mixer.Channel(0) }

    # Volume settings (0.0 - 1.0)
    volumes = {
        'general': Settings.get('sound', 'general'),
        'ui': Settings.get('sound', 'ui'),
        'music': Settings.get('sound', 'music'),
        'sfx': Settings.get('sound', 'sfx'),
    }

    # Cached sound effects
    cache = {}  # filename -> pg.mixer.Sound

    lr.Log.debug('AudioManager initializing...')

    sfx_folder = Path('./sfx')
    for file in sfx_folder.glob('*.mp3'):
        try:
            sound = pg.mixer.Sound(str(file))
            cache[file.name] = sound

            lr.Log.debug(f'Cached SFX: {file.name}')
        except Exception as e:
            lr.Log.error(f'Failed to load sound {file.name}: {e}')

    lr.Log.debug(f'AudioManager initialized with {len(cache)} SFX files.')

    @staticmethod
    def set_volume(group:str, value:float):
        value = max(0.0, min(1.0, value))
        AudioManager.volumes[group] = value

    @staticmethod
    def set_general_volume(value:float):
        AudioManager.volumes['general'] = max(0.0, min(1.0, value))

    @staticmethod
    def get_volume(group:str) -> float:
        return AudioManager.volumes['general'] * AudioManager.volumes[group]

    @staticmethod
    def play(filename:str, group:str = 'sfx', loops:int=0):
        if filename not in AudioManager.cache:
            lr.Log.error(f'Sound "{filename}" not found in cache!')
            return None

        sound = AudioManager.cache[filename]
        sound.set_volume(AudioManager.get_volume(group))

        if group in AudioManager.channels:
            AudioManager.channels[group].play(sound, loops=loops)
        else:
            pg.mixer.find_channel().play(sound, loops=loops)

        return sound