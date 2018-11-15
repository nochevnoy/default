#:kivy 1.10.1

<root>:
    orientation: "vertical"
    size_hint: None, None
    width: 200
    height: 200
    TextInput:
        id: text_1st
        text:"login"
        on_focus: if self.focus: self.text = ""
        on_focus: if not self.focus and self.text == "": self.text = "login"
        
    TextInput:
        id: text_2nd
        text:"password"
        on_focus: if self.focus: self.text = ""
        on_focus: if not self.focus and self.text == "": self.text = "password"

    Button:
        id: btn_2nd
        text: "autorize"

    Button:
        id: btn_3rd
        text: "pass recovery"    






from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class root(BoxLayout):
    pass

class app(App):
    def build(self):
        self.title = "Crush dat man"
        return root()

if __name__ == "__main__":
    app().run()
