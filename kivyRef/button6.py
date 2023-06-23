from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def button_pressed(self, instance):
        instance.text = "Button Pressed!"
        instance.disabled = True

    def build(self):
        button = Button(text='Click Me!', size_hint=(0.5, 0.5),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        button.bind(on_press=self.button_pressed)

        return button


if __name__ == '__main__':
    MyApp().run()
