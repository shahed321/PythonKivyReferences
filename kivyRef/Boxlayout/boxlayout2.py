from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class NestedBoxLayoutApp(App):
    def build(self):
        # Create the outer BoxLayout with horizontal orientation
        outer_layout = BoxLayout(orientation='horizontal')

        # Create the inner BoxLayout with vertical orientation
        inner_layout = BoxLayout(orientation='vertical')

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
    NestedBoxLayoutApp().run()
