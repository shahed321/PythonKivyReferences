from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Click Me!",
                    background_color = (1, 0, 0, 1),
                    color = (0, 1, 0, 1),
                    font_size = 20,
                    size_hint = (0.5, 0.5),
                    pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                    disabled = False
                    )
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    MyApp().run()