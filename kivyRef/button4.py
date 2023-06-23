from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        btn = Button(text="Click Me!",
                     background_normal = 'img/ball.jpg',
                     #background_down = 'button_pressed.png'
                     )
        layout.add_widget(btn)

        return layout

if __name__=="__main__":
    MyApp().run()