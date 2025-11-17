from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


__author__ = "Villacampa Perry Kyle Pepito"

class DynamicLabelsApp(App):
    """Kivy App for dynamically creating labels"""

    def __init__(self, **kwargs):
        """Construct the app, initialising the list of names"""
        super().__init__(**kwargs)
        self.names = ["Perry", "Peter", "Bob", "Jones", "Kyle"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root

DynamicLabelsApp().run()