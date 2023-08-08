from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class NamingRulesApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        variable_with_underscore = 42
        variableWithCamelCase = "Hello"
        Layout = "This is a string"
        myLayout = Label(text="Kivy Naming Rules Example")
        
        layout.add_widget(myLayout)
        
        print(variable_with_underscore)
        print(variableWithCamelCase)
        print(Layout)
        
        return layout

if __name__ == '__main__':
    NamingRulesApp().run()
