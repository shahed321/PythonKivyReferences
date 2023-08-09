from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class SliderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        # Create a label to display the slider value
        self.value_label = Label(text="Slider Value: 0")
        
        # Create a slider with a range of 0 to 100
        self.slider = Slider(min=0, max=100, value=0)
        self.slider.bind(value=self.on_slider_value_change)
        
        # Add the label and slider to the layout
        layout.add_widget(self.value_label)
        layout.add_widget(self.slider)
        
        return layout

    def on_slider_value_change(self, instance, value):
        # Update the label text with the current slider value
        self.value_label.text = f"Slider Value: {int(value)}"

if __name__ == '__main__':
    SliderApp().run()
