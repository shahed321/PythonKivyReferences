from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class StyledBoxLayoutApp(App):
    def build(self):
        # Create the outer BoxLayout with horizontal orientation
        outer_layout = BoxLayout(orientation='horizontal')
        outer_layout.spacing = 10  # Adds spacing between widgets
        outer_layout.padding = [20, 10, 20, 10]  # Sets padding [left, top, right, bottom]

        # Create the inner BoxLayout with vertical orientation
        inner_layout = BoxLayout(orientation='vertical')
        inner_layout.spacing = 5  # Adds spacing between widgets
        inner_layout.padding = [10, 20, 10, 20]  # Sets padding [left, top, right, bottom]

        # Create buttons and add them to the inner layout
        button1 = Button(text='Button 1')
        inner_layout.add_widget(button1)

        button2 = Button(text='Button 2')
        inner_layout.add_widget(button2)

        # Add the inner layout to the outer layout
        outer_layout.add_widget(inner_layout)

        button3 = Button(text='Button 3')
        outer_layout.add_widget(button3)

        return outer_layout


if __name__ == '__main__':
    StyledBoxLayoutApp().run()
