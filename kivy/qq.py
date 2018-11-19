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
        self.hp = 250
        self.damage = 10
        self.crit = 15
        self.mod = 2

    def attack1(self, *args):
        #first player attack
        dmg_done = player1.damage * player1.critx if random.randint(0, 100) <= player1.crit else player1.damage
        player2.hp = player2.hp - dmg_done
        print("Player1 hits {}".format(dmg_done))

    def attack2(self, *args):
        #second player attack
        dmg_done = player2.damage * player2.critx if random.randint(0, 100) <= player2.crit else player2.damage
        player1.hp = player1.hp - dmg_done
        print("Player2 hits {}".format(dmg_done))

    def start_game(self, *args):
        #init players
        player1 = Player()
        player2 = Player()

        self.ids.player1_hp.text = str(player1.hp)
    


class root(FloatLayout, Player):
    pass

class app(App):
    def build(self):
        self.title = "Knights duel rev 1.0"
        return root()

if __name__ == "__main__":
    app().run()
    
    
##########################################################    
    
#:kivy 1.10.1

<root>:
    canvas:
        Rectangle:
            pos: self.center_x - 5, 0
            size: 10, self.height
    Button:
        id: begin
        text: 'Start'
        pos_hint: {'x': 0.01, 'center_y': 0.94}
        color: .12, .66, .95, 1
        background_color: (.53, .89, .38, 1)
        background_normal: ""
        size_hint: .1, .1
        font_size: self.height - dp(25)

        on_press: root.start_game()

    Button:
        id: end
        text: 'Reset'
        pos_hint: {'x': 0.89, 'center_y': 0.94}
        color: .90, .16, .56, 1
        background_color: (.53, .89, .38, 1)
        background_normal: ""
        size_hint: .1, .1
        font_size: self.height - dp(30)
        

    AnchorLayout
        anchor_x: 'left'
        anchor_y: 'top'
        Label:
            id: player1_name
            text: "First Player"
            size_hint: .5, .15
            color: [.1, .79, .97, 1]
            font_size: 30

    AnchorLayout
        anchor_x: 'right'
        anchor_y: 'top'
        Label:
            id: player2_name            
            text: "Second Player"
            size_hint: .5, .15
            color: [.90, .16, .56, 1]
            font_size: 30

    AnchorLayout
        anchor_x: 'left'
        anchor_y: 'center'
        GridLayout
            cols: 3
            rows: 4
            size_hint: .49, .15
            Label:
                text: 'HP'
            Label:
                id: player1_hp
                text: '0'    
            Button:
                id: player1_hp_up
                text:'+'
            Label:
                text: 'Damage'
            Label:
                id: player1_dmg
                text: '0'    
            Button:
                id: player1_dmg_up
                text:'+'
                
            Label:
                text: 'Crit, %'
            Label:
                id: player1_crit
                text: '0'    
            Button:
                id: player1_crit_up
                text:'+'
                
            Label:
                text: 'Crit mod'
            Label:
                id: player1_critm
                text: '0'    
            Button:
                id: player1_critm_up
                text:'+'
                             

    AnchorLayout
        anchor_x: 'right'
        anchor_y: 'center'
        GridLayout
            cols: 3
            rows: 4
            size_hint: .49, .15
            Label:
                text: 'HP'
            Label:
                id: player2_hp
                text: '0'    
            Button:
                id: player2_hp_up
                text:'+'
            Label:
                text: 'Damage'
            Label:
                id: player2_dmg
                text: '0'    
            Button:
                id: player2_dmg_up
                text:'+'
                
            Label:
                text: 'Crit, %'
            Label:
                id: player2_crit
                text: '0'    
            Button:
                id: player2_crit_up
                text:'+'
                
            Label:
                text: 'Crit mod'
            Label:
                id: player2_critm
                text: '0'    
            Button:
                id: player2_critm_up
                text:'+'

    AnchorLayout
        anchor_x: 'left'
        anchor_y: 'bottom'
        BoxLayout:
            size_hint: .49, .25
            orientation: 'vertical'
            Button:
                id: player1_attack
                text:'Crush!'
            Label:
                id: player1_log
                text: 'Log is here'


    AnchorLayout
        anchor_x: 'right'
        anchor_y: 'bottom'
        BoxLayout:
            size_hint: .49, .25
            orientation: 'vertical'
            Button:
                id: player2_attack
                text:'Crush!'
            Label:
                id: player2_log
                text: 'Log is here'
