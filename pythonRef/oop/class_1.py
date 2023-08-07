from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Enemy:
    life = 3

    def attack(self):
        print("Ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            return "I'm dead"
        else:
            return str(self.life) + " life left"

class MyApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create an instance of Enemy class
        enemy = Enemy()

        # Create label and button objects
        label = Label(text=enemy.checkLife())
        button = Button(text='Attack', on_release=self.on_button_release)

        # Add label and button to the layout
        layout.add_widget(label)
        layout.add_widget(button)

        # Store the enemy instance in the app object
        self.enemy = enemy

        # Return the layout as the root widget
        return layout

    def on_button_release(self, button):
        self.enemy.attack()
        label = self.root.children[0]  # Assuming label is the first child widget
        label.text = self.enemy.checkLife()

if __name__ == '__main__':
    MyApp().run()
