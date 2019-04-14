from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from kivy.uix.popup import Popup

import player

player.players()
class MainApp(App):
    def out(self, obj):
        lb = Label(text = 'check')
        for i in range(player.CurNumOfGamers):
            for j in player.qplayers:
                for k in j:
                    print(k)
        return lb 

    def pressCallback(self, btn):
        Popup(on_dismiss=self.out).open()

    def build(self):
        gl = GridLayout(cols = 3)
        for i in range(player.CurNumOfGamers):
            btn = Button(text='Player' + str(i+1))
            btn.bind(on_press = self.pressCallback)
            gl.add_widget(btn)

        return gl
MainApp().run()