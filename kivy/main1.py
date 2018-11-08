import random

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


from kivy.config import Config
Config.set("graphics", "resizable", "1")
Config.set("graphics", "width", "640")
Config.set("graphics", "heigth", "480")


class Player():
    """
    Player's stats and moves
    """
    def __init__(self):
        self.hp = 100
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

#init players
player1 = Player()
player2 = Player()

class CrushApp(App, Player):
    """
    main app class
    """
    def build(self):
        self.title = "Crush that man"

        root = BoxLayout(orientation = "horizontal")    #main frame
        left = BoxLayout(orientation = "vertical", size_hint = (0.5, 0.8))    #left side of main window
        right = BoxLayout(orientation = "vertical", size_hint = (0.5, 0.8))    #right side of main window
        #player names
        fplayername = Label(text = "First Player", font_size = 30, color = [.1, .79, .97, 1], size_hint = (1, 0.07))
        splayername = Label(text = "Second Player", font_size = 30, color = [.90, .16, .56, 1], size_hint = (1, 0.07))
        left.add_widget(fplayername)
        right.add_widget(splayername)
        #player stats frame
        fplayerstats = GridLayout(cols = 3, rows = 3, size_hint = (1, 0.8))
        splayerstats = GridLayout(cols = 3, rows = 3, size_hint = (1, 0.8))
        left.add_widget(fplayerstats)
        right.add_widget(splayerstats)
        # first player stats
        fplayerhpl = Label(text = "HP:")
        fplayerdmgl = Label(text = "Damage:")
        fplayercritl = Label(text = "Crit [%]:")

        fplayerhpb = Button(text = "#", background_color = [.1, .79, .97, 1] ,size_hint = (1,.1))
        fplayerdmgb = Button(text = "##", background_color = [.1, .79, .97, 1], size_hint = (1,.1))
        fplayercritb = Button(text = "###", background_color = [.1, .79, .97, 1] ,size_hint = (1,.1))

        fplayerhpv = Label(text = str(player1.hp))
        fplayerdmgv = Label(text = str(player1.damage))
        fplayercritv = Label(text = str(player1.crit))

        fplayerstats.add_widget(fplayerhpl)
        fplayerstats.add_widget(fplayerhpv)
        fplayerstats.add_widget(fplayerhpb)

        fplayerstats.add_widget(fplayerdmgl)
        fplayerstats.add_widget(fplayerdmgv)
        fplayerstats.add_widget(fplayerdmgb)

        fplayerstats.add_widget(fplayercritl)
        fplayerstats.add_widget(fplayercritv)
        fplayerstats.add_widget(fplayercritb)
        #second player stats
        splayerhpl = Label(text = "HP:")
        splayerdmgl = Label(text = "Damage:")
        splayercritl = Label(text = "Crit [%]:")

        splayerhpb = Button(text = "#", background_color = [.90, .16, .56, 1], size_hint = (1,.1))
        splayerdmgb = Button(text = "##", background_color = [.90, .16, .56, 1], size_hint = (1,.1))
        splayercritb = Button(text = "###", background_color = [.90, .16, .56, 1], size_hint = (1,.1))

        splayerhpv = Label(text = str(player2.hp))
        splayerdmgv = Label(text = str(player2.damage))
        splayercritv = Label(text = str(player2.crit))

        splayerstats.add_widget(splayerhpl)
        splayerstats.add_widget(splayerhpv)
        splayerstats.add_widget(splayerhpb)

        splayerstats.add_widget(splayerdmgl)
        splayerstats.add_widget(splayerdmgv)
        splayerstats.add_widget(splayerdmgb)

        splayerstats.add_widget(splayercritl)
        splayerstats.add_widget(splayercritv)
        splayerstats.add_widget(splayercritb)

        root.add_widget(left)
        root.add_widget(right)
        return root

if __name__ == '__main__':
    CrushApp().run()



