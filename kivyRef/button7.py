from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def button_pressed(self, instance):
        print("Button Pressed!")

    def bind_button(self, instance):
        instance.bind(on_press=self.button_pressed)
        print("Button bound to on_press event.")

    def unbind_button(self, instance):
        instance.unbind(on_press=self.button_pressed)
        print("Button unbound from on_press event.")

    def build(self):
        root = BoxLayout(orientation='vertical')

        button = Button(text='Click Me!')
        bind_button = Button(text='Bind')
        unbind_button = Button(text='Unbind')

        bind_button.bind(on_press=self.bind_button)
        unbind_button.bind(on_press=self.unbind_button)

        root.add_widget(button)
        root.add_widget(bind_button)
        root.add_widget(unbind_button)

        return root


if __name__ == '__main__':
    MyApp().run()
