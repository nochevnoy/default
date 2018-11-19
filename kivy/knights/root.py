import random

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout



class Player():
    """
    Player's stats and moves
    """
    def __init__(self):
        self.hp = 500
        self.damage = 10
        self.crit = 25
        self.mod = 2
        self.points = 10

    def attack1(self, *args):
        #first player attack
        dmg_done = player1.damage * player1.mod if random.randint(0, 100) <= player1.crit else player1.damage
        player2.hp = player2.hp - dmg_done
        
        self.ids.player2_hp.text = str(player2.hp)
        self.ids.player1_log.text = "Player1 hits {}".format(dmg_done)

        print("Player1 hits {}".format(dmg_done))

    def attack2(self, *args):
        #second player attack
        dmg_done = player2.damage * player2.mod if random.randint(0, 100) <= player2.crit else player2.damage
        player1.hp = player1.hp - dmg_done
        
        self.ids.player1_hp.text = str(player1.hp)
        self.ids.player2_log.text = "Player2 hits {}".format(dmg_done)

        print("Player2 hits {}".format(dmg_done))

    def start_game(self, *args):
        #init players   
        global player1, player2

        player1 = Player()
        player2 = Player()

        self.ids.player1_hp.text = str(player1.hp)
        self.ids.player1_dmg.text = str(player1.damage)
        self.ids.player1_crit.text = str(player1.crit)
        self.ids.player1_critm.text = str(player1.mod)

        self.ids.player2_hp.text = str(player2.hp)
        self.ids.player2_dmg.text = str(player2.damage)
        self.ids.player2_crit.text = str(player2.crit)
        self.ids.player2_critm.text = str(player2.mod)

    def reset_game(self, *args):
        #reset all numbers
        self.ids.player1_log.text = 'Log is here'
        self.ids.player2_log.text = 'Log is here'
        return self.start_game()

        
class root(FloatLayout, Player):
    pass

class app(App):
    def build(self):
        self.title = "Knights duel rev 1.0"
        return root()

if __name__ == "__main__":
    app().run()
