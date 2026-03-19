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
    def is_high_score(score:int) -> bool:
        """
        **Check if the passed score is the highest.**
        
        *Parameters*:
        - `score` (int): The score to compare.
        
        *Returns*:
        - (bool): Is the highest score.
        """

        data = Leaderboard.get()
        if not data:
            return True

        return score > max(data.values(), default=0)

    @staticmethod
    def upsert(username:str, score:int):
        """
        **Insert/Update a users saved score.**
        
        *Parameters*:
        - `username` (str): Username of the player
        - `score` (int): New score to set
        """

        lr.Log.debug(f'Writing leaderboard: {username}={score}')

        # Grab fresh data
        data = Leaderboard.get()
        if not data:
            return
        
        # Upsert the name
        data[username] = score

        with open(Leaderboard._settings_path, 'w') as file:
            json.dump(data, file, indent=4)