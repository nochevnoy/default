import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


from kivy.config import Config
Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "800")
Config.set("graphics", "heigth", "600")





class Player():
    def __init__(self):
        self.hp = 100
        self.damage = 10
        self.crit = 30
        self.critx = 2
    
    def roll1(self, *args):
        dmg_done = player1.damage * player1.critx if random.randint(0, 100) <= player1.crit else player1.damage
        player2.hp = player2.hp - dmg_done
        print("Player1 hits {}".format(dmg_done))

    def roll2(self, *args):
        dmg_done = player2.damage * player2.critx if random.randint(0, 100) <= player2.crit else player2.damage
        player1.hp = player1.hp - dmg_done
        print("Player2 hits {}".format(dmg_done))     

player1 = Player()
player2 = Player()

class CrushApp(App, Player):
    def build(self):
        self.title = "Crush dat man"
        root = BoxLayout(orientation = "horizontal")    #main window frame
        left = BoxLayout(orientation = "vertical")    #left side of main window
        right = BoxLayout(orientation = "vertical")    #right side of main window

        #player names
        fplayername = Label(text = "First Player", font_size = 30, color = [.1, .79, .97, 1], size_hint = (1, 0.5))
        splayername = Label(text = "Second Player", font_size = 30, color = [.90, .16, .56, 1], size_hint = (1, 0.5))
        roll1 = Button(text = "Player1 rolls", on_press = self.roll1, size_hint = (1, 0.2))
        roll2 = Button(text = "Player2 rolls", on_press = self.roll2, size_hint = (1, 0.2))
        left.add_widget(fplayername)
        left.add_widget(roll1)
        right.add_widget(splayername)
        right.add_widget(roll2)

        #player stats
        fplayerstats = BoxLayout(orientation = "vertical", size_hint = (1, 0.25))
        splayerstats = BoxLayout(orientation = "vertical", size_hint = (1, 0.25))
            #HP
        fplayerhp = Label(text = "HP:  {}".format(player1.hp))
        splayerhp = Label(text = "HP:  {}".format(player2.hp))
        fplayerstats.add_widget(fplayerhp)
        splayerstats.add_widget(splayerhp)
            #DMG
        fplayerdmg = Label(text = "Damage:  {}".format(player1.damage))
        splayerdmg = Label(text = "Damage:  {}".format(player2.damage))
        fplayerstats.add_widget(fplayerdmg)
        splayerstats.add_widget(splayerdmg)
            #CRIT chance
        fplayercrit = Label(text = "Crit %:  {}".format(player1.crit))
        splayercrit = Label(text = "Crit %:  {}".format(player2.crit))
        fplayerstats.add_widget(fplayercrit)
        splayerstats.add_widget(splayercrit)

        left.add_widget(fplayerstats)
        right.add_widget(splayerstats)

        #player log
        fplayerlog = BoxLayout(orientation = "vertical")
        splayerlog = BoxLayout(orientation = "vertical")
        left.add_widget(fplayerlog)
        right.add_widget(splayerlog)   

        root.add_widget(left)
        root.add_widget(right)
        return root

if __name__ == '__main__':
    CrushApp().run()
    

