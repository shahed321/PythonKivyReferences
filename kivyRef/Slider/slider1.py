from kivy.app import App
from kivy.uix.slider import Slider

class SliderApp(App):
    def build(self):
        # Create a slider with a range of 0 to 100
        slider = Slider(min=0, max=100)
        return slider

if __name__ == '__main__':
    SliderApp().run()
