from kivy.app import App
from kivy.uix.image import Image

class MyImageApp(App):
    def build(self):
        # Create an Image widget
        image = Image(source='your_image_file.png')  # Replace with your image file path
        
        return image

if __name__ == '__main__':
    MyImageApp().run()
