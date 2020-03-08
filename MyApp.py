from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class container(GridLayout):

    krac = ObjectProperty()
    lb_widget = ObjectProperty()

    def change_text(self):
        self.lb_widget.text = self.krac.text.upper()

class MyApp(App):
    def build(self):
        return container()

if __name__ == '__main__':
    MyApp().run()