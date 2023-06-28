import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from functools import partial

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Hello, Kivy!")
        layout.add_widget(label)
        
        button = Button(text="Click Me!")
        button.bind(on_press=partial(self.on_button_click, "Additional Argument", 42))
        layout.add_widget(button)
        
        return layout

    def on_button_click(self, additional_arg, int_arg, instance):
        instance.text = "Button Clicked!"
        print("Additional argument:", additional_arg)
        print("Integer argument:", int_arg)

if __name__ == '__main__':
    MyApp().run()
