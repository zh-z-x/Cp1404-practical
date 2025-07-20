from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name and add to GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

if __name__ == '__main__':
    DynamicLabelsApp().run()