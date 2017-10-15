from datetime import datetime, timedelta

class Pubg(object):

    def __init__(self):
        self.top_history = []
    
    def _last_top(self, players=None):
        if not players:
            if self.top_history:
                return self.top_history[-1]
            else:
                return None
        for top in self.top_history:
            print(top['players'] == players)
            if top['players'] == players:
                return top

    def get_last(self, players=None):
        now = datetime.now()
        if players:
            top = self._last_top(players)
        else:
            top = self._last_top()

        if top:
            msg = 'Last top for team ' + ' '.join(top['players'].split(',')) + ' was ' + str(now - top['time']) + ' ago'
        else:
            msg = 'No last top'
            if players:
                msg += ' for this team'

        self._remove_old()
        return msg

    def new_top(self, players):
        top = {
            'time': datetime.now(),
            'players': players
        }
        self.top_history.append(top)
        print(self.top_history)
        self._remove_old()

    def _remove_old(self):
        now = datetime.now()
        for top in self.top_history:
            if top['time'] < now - timedelta(days=30):
                self.top_history.remove(top)