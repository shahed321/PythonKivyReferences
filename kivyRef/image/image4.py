from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class MyImageAdjustmentApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create an Image widget with adjustments
        image = Image(
            source='../img/ball.jpg',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(None, None),  # Disable automatic size_hint adjustments
            size=(200, 200),  # Set a specific size
            color=(1, 0.5, 0.5, 1),  # Apply a reddish tint
            opacity=0.8,  # Set opacity to 80%
        )
        
        layout.add_widget(image)
        
        return layout

if __name__ == '__main__':
    MyImageAdjustmentApp().run()
