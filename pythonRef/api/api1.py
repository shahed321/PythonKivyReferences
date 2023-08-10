import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

kivy.require('1.11.1')  # Make sure to use the appropriate Kivy version

class APIApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="API Data will appear here")
        self.fetch_button = Button(text="Fetch API Data", on_press=self.fetch_data)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.fetch_button)
        
        return self.layout
    
    def fetch_data(self, instance):
        api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example API endpoint
        
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            self.label.text = f"API Data:\n{data}"
        else:
            self.label.text = "Error fetching API data"

if __name__ == '__main__':
    app = APIApp()
    app.run()
