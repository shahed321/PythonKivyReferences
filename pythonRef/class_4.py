from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Mario:
    def move(self, distance):
        return f"I'm moving {distance}m"

class Shroom:
    def eat_shroom(self):
        return 'Now I am big!'

class BigMario(Mario, Shroom):
    pass

class MyApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create an instance of BigMario class
        bm = BigMario()

        # Create label and button objects
        label1 = Label(text='Mario Actions:')
        button1 = Button(text='Move', on_release=self.on_move_release)
        label2 = Label(text='Shroom Actions:')
        button2 = Button(text='Eat Shroom', on_release=self.on_shroom_release)

        # Add labels and buttons to the layout
        layout.add_widget(label1)
        layout.add_widget(button1)
        layout.add_widget(label2)
        layout.add_widget(button2)

        # Store the BigMario instance in the app object
        self.bm = bm

        # Store the label widget in the app object
        self.distance_label = label1

        # Return the layout as the root widget
        return layout

    def on_move_release(self, button):
        distance = 5  # Distance can be changed as per your requirements
        self.distance_label.text = self.bm.move(distance)

    def on_shroom_release(self, button):
        self.distance_label.text = self.bm.eat_shroom()

if __name__ == '__main__':
    MyApp().run()
