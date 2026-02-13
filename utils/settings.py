import loggerric as lr
import os, json

class Settings:
    """
    **Handles settings reading/writing.**
    
    Writes and read to/from the settings file while catching erros, and
    automatically creating key nests.
    
    *Methods*:
    - `get(*keys) -> any`: Returns the parsed value in the key nest location.
    - `set(value, *keys) -> None`: Sets the value the key nest points to.
    """

    # Full path to the settings file
    _settings_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'settings.json')

    # Keep track of the latest data as to not make too many open() calls
    _latest_data = None

    lr.Log.debug('Settings initialized!')

    @staticmethod
    def get(*keys):
        """
        **Get a key nest value.**
        
        *Parameters*:
        - `*keys` (str): Keys leading to the target value.
        
        *Returns*:
        - (any): The data stored in the key nest target.
        """

        try:
            with open(Settings._settings_path, 'r') as file:
                data:dict = json.load(file)

                # Update cache
                Settings._latest_data = data

                for key in keys:
                    # If the key points to nothing, return empty
                    if data == None:
                        return

                    data = data.get(key)
        except Exception as e:
            lr.Log.error('Error reading [{}]: {}'.format('.'.join(keys), e))
            return
        
        lr.Log.debug('Reading:', '.'.join(keys), '= {}'.format(
            data if len(str(data)) < 20 else f'{str(data)[:20]}...'))

        return data

    def set(value, *keys) -> None:
        """
        **Set the value of a key nests target.**
        
        *Parameters*:
        - `value` (any): The value that should be set.
        - `*keys` (str): The keys pointing to the target location.
        """
        lr.Log.debug('Writing:', '.'.join(keys), f'= {value}')

        # Grab the currently stored data from the cache, or read from the file
        if Settings._latest_data:
            data = Settings._latest_data
        else:
            with open(Settings._settings_path, 'r') as file:
                data:dict = json.load(file)
        
        # Create a pointer, as to not lose root reference (data)
        section = data

        # Iterate all but the last key
        for key in keys[:-1]:
            section = section.setdefault(key, {})
        
        # Assign new value to the final key in the nest
        section[keys[-1]] = value

        with open(Settings._settings_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        # Update cache
        Settings._latest_data = data