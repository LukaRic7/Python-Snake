import loggerric as lr
import os, json

class Leaderboard:
    _settings_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'leaderboard.json')

    lr.Log.debug('Leaderboard initialized!')

    @staticmethod
    def get() -> dict:
        try:
            with open(Leaderboard._settings_path, 'r') as file:
                data:dict = json.load(file)

                sorted_keys = sorted(data, key=lambda k: data[k], reverse=True)
                sorted_data = { k: data[k] for k in sorted_keys }
        except Exception as e:
            lr.Log.error(f'Error reading leaderboard: {e}')
            return

        lr.Log.debug(f'Read {len(data):,} leaderboard keys.')
    
        return sorted_data

    @staticmethod
    def upsert(username:str, score:int):
        lr.Log.debug(f'Writing leaderboard: {username}={score}')

        # Grab fresh data
        data = Leaderboard.get()
        if not data:
            return
        
        # Upsert the name
        data[username] = score

        with open(Leaderboard._settings_path, 'w') as file:
            json.dump(data, file, indent=4)