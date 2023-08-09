from kivy.app import App
from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        # Create a switch widget
        switch = Switch(active=False)
        return switch

if __name__ == '__main__':
    SwitchApp().run()
