import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create Label widget
        self.label = Label(text='Entered text will be displayed here.')

        # Create TextInput widget
        self.text_input = TextInput(multiline=False)
        self.text_input.bind(on_text_validate=self.on_enter)

        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)

        return layout

    def on_enter(self, instance):
        self.label.text = self.text_input.text


if __name__ == '__main__':
    MyApp().run()
