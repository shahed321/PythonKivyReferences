from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        button1 = Button(text='Click Me 1!', size_hint=(0.5, 0.5),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(button1)

        button2 = Button(text='Click Me 2!', size_hint=(0.5, 0.5),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(button2)

        return layout


if __name__ == '__main__':
    MyApp().run()
