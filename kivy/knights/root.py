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
        self.points = 5
        self.turn = 0

    def attack1(self, *args):
        #first player attack
        if player1.turn == 1:
            dmg_done = player1.damage * player1.mod if random.randint(0, 100) <= player1.crit else player1.damage
            player2.hp = player2.hp - dmg_done
        
            self.ids.player2_hp.text = str(player2.hp)
            self.ids.player1_log.text = "Player1 hits {}".format(dmg_done)

            print("Player1 hits {}".format(dmg_done))
            
            player1.turn -= 1
            player2.turn += 1
            player1.points += 5
            

            self.ids.player2_turn.text = 'YOUR TURN!'
            self.ids.player1_turn.text = ''
        else:
            self.ids.player1_log.text = 'ITS NOT YOUR TURN NOW'
        self.ids.player1_points.text = str(player1.points)

    def attack2(self, *args):
        #second player attack
        if player2.turn == 1:
            dmg_done = player2.damage * player2.mod if random.randint(0, 100) <= player2.crit else player2.damage
            player1.hp = player1.hp - dmg_done
        
            self.ids.player1_hp.text = str(player1.hp)
            self.ids.player2_log.text = "Player2 hits {}".format(dmg_done)

            print("Player2 hits {}".format(dmg_done))
            
            player2.turn -= 1
            player1.turn += 1
            player2.points += 5
            

            self.ids.player1_turn.text = 'YOUR TURN!'
            self.ids.player2_turn.text = ''
        else:
            self.ids.player2_log.text = 'ITS NOT YOUR TURN NOW'
        self.ids.player2_points.text = str(player2.points)

    def wturn(self, *args):
        # who ll be first? 0 = 1player, 1 = 2player
        global two
        two = [0, 1]

        if random.choice(two) == 0:
            player1.turn = 1
            self.ids.player1_turn.text = 'YOUR TURN!'
        else:
            player2.turn = 1
            self.ids.player2_turn.text = 'YOUR TURN!'

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

        self.ids.player1_points.text = str(player1.points)
        self.ids.player2_points.text = str(player2.points)

        return self.wturn()

    def reset_game(self, *args):
        #reset all numbers
        self.ids.player1_log.text = 'Log is here'
        self.ids.player2_log.text = 'Log is here'
        self.ids.player1_turn.text = ''
        self.ids.player2_turn.text = ''
        return self.start_game()

    def hp1(self, *args):
        # first player add hp
        if player1.points > 0:
            player1.hp += 25
            player1.points -= 1
            self.ids.player1_hp.text = str(player1.hp)
            self.ids.player1_points.text = str(player1.points)
        else:
            self.ids.player1_log.text = "YOU DONT HAVE ANY POINTS"

    def dmg1(self, *args):
        # first player add dmg
        if player1.points > 0:
            player1.damage += 5
            player1.points -= 1
            self.ids.player1_dmg.text = str(player1.damage)
            self.ids.player1_points.text = str(player1.points)
        else:
            self.ids.player1_log.text = "YOU DONT HAVE ANY POINTS"

    def crit1(self, *args):
        # first player add crit
        if player1.points > 0:
            player1.crit += 3
            player1.points -= 1
            self.ids.player1_crit.text = str(player1.crit)
            self.ids.player1_points.text = str(player1.points)
        else:
            self.ids.player1_log.text = "YOU DONT HAVE ANY POINTS"

    
    def hp2(self, *args):
        # second player add hp
        if player2.points > 0:
            player2.hp += 25
            player2.points -= 1
            self.ids.player2_hp.text = str(player2.hp)
            self.ids.player2_points.text = str(player2.points)
        else:
            self.ids.player2_log.text = "YOU DONT HAVE ANY POINTS"

    def dmg2(self, *args):
        # second player add dmg
        if player2.points > 0:
            player2.damage += 5
            player2.points -= 1
            self.ids.player2_dmg.text = str(player2.damage)
            self.ids.player2_points.text = str(player2.points)
        else:
            self.ids.player2_log.text = "YOU DONT HAVE ANY POINTS"

    def crit2(self, *args):
        # second player add crit
        if player2.points > 0:
            player2.crit += 3
            player2.points -= 1
            self.ids.player2_crit.text = str(player2.crit)
            self.ids.player2_points.text = str(player2.points)
        else:
            self.ids.player2_log.text = "YOU DONT HAVE ANY POINTS"

    


    

        
class root(FloatLayout, Player):
    pass

class app(App):
    def build(self):
        self.title = "Knights duel rev 1.0"
        return root()

if __name__ == "__main__":
    app().run()
