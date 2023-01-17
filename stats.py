import json

class Stats:
    def __init__(self):
        self._reset_stats()
        file = 'data/best_score.json'
        with open(file) as f:
            self.best_score = json.load(f)
        
    def _reset_stats(self):
        self.game_is_active = False
        self.button_clicked = False
        self.speed_choosed = False
        self.score = 0