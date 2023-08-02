from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        # Creating a button instance
        button = Button(text='Click Me!', size_hint=(0.5, 0.5),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        return button


if __name__ == '__main__':
    MyApp().run()
