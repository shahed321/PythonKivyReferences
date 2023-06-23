from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class MyPopup(Popup):
    pass

class MyApp(App):
    def build(self):
        # Create a label widget
        label = Label(text="Click the button to open the popup!")

        # Create a popup instance
        popup = MyPopup(title='My Popup', size_hint=(None, None), size=(400, 400))

        # Create a separate label for the popup content
        popup_label = Label(text="Popup Content")

        # Set the content of the popup
        popup.content = popup_label

        # Create a button to open the popup
        button = Button(text="Open Popup", on_release=popup.open)

        # Add the button to the layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
