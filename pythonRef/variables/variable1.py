from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.count = 0  # Initialize a variable
        
        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Count: 0")
        layout.add_widget(self.label)
        
        button = Button(text="Increment Count")
        button.bind(on_press=self.increment_count)
        layout.add_widget(button)
        
        return layout

    def increment_count(self, instance):
        self.count += 1
        self.label.text = "Count: {}".format(self.count)

if __name__ == '__main__':
    MyApp().run()
