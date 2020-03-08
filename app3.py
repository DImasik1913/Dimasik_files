from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.core.window import Window

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,1,0,1)
            rad = 10
            Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size = (rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
    
    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

class MyGameApp(App):
    def build(self):
        perent = Widget()
        self.paint = Painter()
        perent.add_widget(self.paint)
        
        perent.add_widget(Button(text = 'Clear', on_press = self.clear_canvas, size = (100, 50)))
        perent.add_widget(Button(text = 'Save', on_press = self.save, size = (100, 50), pos = (100, 0)))
        perent.add_widget(Button(text = 'Screenshot', on_press = self.screenshot, size = (100, 50), pos = (200, 0)))

        return perent
    
    def clear_canvas(self, isinstance):
        self.paint.canvas.clear()
    
    def save(self, isinstance):
        self.paint.size = (Window.size[0], Window.size[1])
        self.paint.export_to_png('image.png')
    
    def screenshot(self, isinstance):
        Window.screenshot('screen.png')

if __name__ == "__main__":
    MyGameApp().run()