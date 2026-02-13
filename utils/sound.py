from pathlib import Path
import loggerric as lr
import pygame as pg

from utils.settings import Settings

class AudioManager:
    """
    **Handles all audio.**
    
    Full sound group volume control, aswell as still having concurrent sounds.
    Caches soundfiles to save memory and time.
    
    *Methods*:
    - `set_volumne(group:str, value:float) -> None`: Sets volume of a group.
    - `set_general_volume(value:float) -> None`: Sets the general volume.
    - `get_volume(group:str) -> float`: Gets a groups current volume.
    - `play(filename:str, group:str = 'sfx', loops:int=0) -> None`: Plays a
    sound in the specified group and with the specified amount of loops.
    """

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
    cache:dict[str, pg.mixer.Sound] = {}

    lr.Log.debug('AudioManager initializing...')

    # Load all files from the sfx folder
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
        """
        **Sets volume of a group**
        
        *Parameters*:
        - `group` (str): Group to set the volume of.
        - `value` (float): Sound value to set (0.0 - 1.0)
        """

        value = max(0.0, min(1.0, value))
        AudioManager.volumes[group] = value

    @staticmethod
    def set_general_volume(value:float):
        """
        **Sets the general volumne.**
        
        *Parameters*:
        - `value` (float): The value to set the volume at.
        """

        AudioManager.volumes['general'] = max(0.0, min(1.0, value))

    @staticmethod
    def get_volume(group:str) -> float:
        """
        **Gets the volume of a group.**
        
        *Parameters*:
        - `group` (str): Group to get the volume of.
        
        *Returns*:
        - (float): Volume of the group (0.0 - 1.0)
        """

        return AudioManager.volumes['general'] * AudioManager.volumes[group]

    @staticmethod
    def play(filename:str, group:str='sfx', loops:int=0):
        """
        **Plays a soundfile stored in the cache.**
        
        *Parameters*:
        - `filename` (str): Filename of the file to play (only name + ext)
        - `group` (str): Group the sound should be played in.
        - `loops` (int=0): How many loops the sound should play (-1 = inf)
        """

        # Check if the sound is stored in the cache
        if filename not in AudioManager.cache:
            lr.Log.error(f'Sound "{filename}" not found in cache!')
            return None

        # Get the sound and set its volume
        sound = AudioManager.cache[filename]
        sound.set_volume(AudioManager.get_volume(group))

        # Check if its a AM channel or PG channel
        if group in AudioManager.channels:
            AudioManager.channels[group].play(sound, loops=loops)
        else:
            pg.mixer.find_channel().play(sound, loops=loops)

        return sound