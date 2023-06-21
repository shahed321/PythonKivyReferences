import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        # Create a BoxLayout as the root widget with a background color
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.canvas.before.add(Color(0.8, 0.8, 0.8, 1))
        layout.canvas.before.add(Rectangle(pos=layout.pos, size=layout.size))

        # Create a Label widget
        label = Label(text='Hello, Kivy!',
                      font_size=40,
                      color=(1, 0, 0, 1),  # Red color
                      bold=True,  # Bold font
                      italic=True,  # Italic font
                      underline=True,  # Underlined text
                      halign='center',  # Horizontal alignment (centered)
                      valign='middle',  # Vertical alignment (middle)
                      size_hint=(1, 1))

        # Add the label widget to the layout
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    MyApp().run()
