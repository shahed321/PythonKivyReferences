from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class ColorMixerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        # Create sliders for red, green, and blue components
        self.red_slider = Slider(min=0, max=1, value=0.5)
        self.green_slider = Slider(min=0, max=1, value=0.5)
        self.blue_slider = Slider(min=0, max=1, value=0.5)
        
        # Create a label to display the color values
        self.color_label = Label(text="Color (R: 0.5, G: 0.5, B: 0.5)")
        
        # Bind slider values to color update function
        self.red_slider.bind(value=self.update_color)
        self.green_slider.bind(value=self.update_color)
        self.blue_slider.bind(value=self.update_color)
        
        # Add sliders and label to the layout
        layout.add_widget(self.red_slider)
        layout.add_widget(self.green_slider)
        layout.add_widget(self.blue_slider)
        layout.add_widget(self.color_label)
        
        # Create a colored rectangle to show the selected color
        with layout.canvas:
            self.color_instruction = Color(0.5, 0.5, 0.5)
            self.color_rectangle = Rectangle(size=(300, 100), pos=(50, 50))
        
        return layout

    def update_color(self, instance, value):
        # Update the color of the rectangle and color label
        color = (self.red_slider.value, self.green_slider.value, self.blue_slider.value)
        self.color_instruction.rgb = color
        self.color_label.text = f"Color (R: {color[0]:.2f}, G: {color[1]:.2f}, B: {color[2]:.2f})"

if __name__ == '__main__':
    ColorMixerApp().run()
