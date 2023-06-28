import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Hello, Kivy!")
        layout.add_widget(label)
        
        button = Button(text="Click Me!")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)
        
        return layout

    def on_button_click(self, instance):
        instance.text = "Button Clicked!"

if __name__ == '__main__':
    MyApp().run()
