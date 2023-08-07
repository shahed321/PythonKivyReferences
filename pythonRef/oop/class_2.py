from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Girl:
    gender = 'female'

    def __init__(self, name):
        self.name = name

class MyApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create an instance of Girl class
        girl = Girl('Rufaidah')

        # Create label widgets
        gender_label = Label(text=f"Gender: {girl.gender}")
        name_label = Label(text=f"Name: {girl.name}")

        # Add labels to the layout
        layout.add_widget(gender_label)
        layout.add_widget(name_label)

        # Return the layout as the root widget
        return layout

if __name__ == '__main__':
    MyApp().run()
