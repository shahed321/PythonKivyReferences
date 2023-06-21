import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        # Create a FloatLayout as the root widget
        layout = FloatLayout()

        # Create a Label widget
        label = Label(text='Hello, Kivy!',
                      font_size=40,
                      color=(1, 0, 0, 1),  # Red color
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})  # Centered position

        # Add the label widget to the layout
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    MyApp().run()