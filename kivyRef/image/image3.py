from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class MyImageLayoutApp(App):
    def build(self):
        # Create a BoxLayout as the root layout
        layout = BoxLayout(orientation='vertical')
        
        # Create an Image widget and add it to the layout
        image = Image(source='../img/ball.jpg')  
        layout.add_widget(image)
        
        return layout

if __name__ == '__main__':
    MyImageLayoutApp().run()
