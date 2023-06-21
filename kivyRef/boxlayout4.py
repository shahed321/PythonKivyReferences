from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class InnerBoxLayout(BoxLayout):
    def __init__(self, orientation='vertical', **kwargs):
        super(InnerBoxLayout, self).__init__(**kwargs)

        self.orientation = orientation

        label = Label(text='Inner BoxLayout')
        self.add_widget(label)

        button1 = Button(text='Button 1')
        self.add_widget(button1)


class OuterBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(OuterBoxLayout, self).__init__(**kwargs)

        label = Label(text='Outer BoxLayout')
        self.add_widget(label)

        inner_layout = InnerBoxLayout(orientation='horizontal')
        self.add_widget(inner_layout)


class NestedBoxLayoutApp(App):
    def build(self):
        return OuterBoxLayout()


if __name__ == '__main__':
    NestedBoxLayoutApp().run()
