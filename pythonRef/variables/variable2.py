from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Enter your name:")
        self.text_input = TextInput()
        self.button = Button(text="Submit", on_press=self.on_submit)
        self.result_label = Label(text="")
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.result_label)
        
        return self.layout
    
    def on_submit(self, instance):
        user_name = self.text_input.text
        if user_name:
            self.result_label.text = f"Hello, {user_name}!"
        else:
            self.result_label.text = "Please enter a name."
        
if __name__ == '__main__':
    MyApp().run()
