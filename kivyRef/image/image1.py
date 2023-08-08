from kivy.app import App
from kivy.uix.image import Image

class MyImageApp(App):
    def build(self):
        
        image = Image(source='../img/ball.jpg')
        
        return image

if __name__ == '__main__':
    MyImageApp().run()
