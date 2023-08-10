import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

kivy.require('1.11.1')  # Make sure to use the appropriate Kivy version

class PrimeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.progress_bar = ProgressBar(max=4)  # Number of primes
        self.layout.add_widget(self.progress_bar)
        
        self.primes = [2, 3, 5, 7]  # List of prime numbers
        self.index = 0
        Clock.schedule_interval(self.process_next_prime, 1)  # Schedule prime processing
        
        return self.layout
    
    def process_next_prime(self, dt):
        if self.index < len(self.primes):
            prime = self.primes[self.index]
            print(prime)  # Replace with your desired action
            
            self.index += 1
            self.progress_bar.value = self.index
            
        else:
            print("All primes processed.")
            self.stop_processing()
    
    def stop_processing(self):
        Clock.unschedule(self.process_next_prime)

if __name__ == '__main__':
    app = PrimeApp()
    app.run()
