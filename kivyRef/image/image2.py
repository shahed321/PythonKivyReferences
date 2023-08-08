from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class ImageExample(BoxLayout):
    def __init__(self, **kwargs):
        super(ImageExample, self).__init__(**kwargs)
        
        # Create an Image widget
        self.image = Image(source='../img/ball.jpg')
        
        # Add the Image widget to the layout
        self.add_widget(self.image)


class MyApp(App):
    def build(self):
        return ImageExample()


if __name__ == '__main__':
    MyApp().run()
