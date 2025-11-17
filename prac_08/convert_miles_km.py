"""
CP1404 Practical - Convert Miles to Km
Villacampa Perry Kyle Pepito
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    """Kivy App for converting miles to km."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the Kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handles the calculation of the text."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handles the up and down button press, update the text input with a new value"""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKm().run()
