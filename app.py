from kivymd.app import MDApp
from kivy.lang import Builder

class ButtonApp(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def action(self):
        label = self.root.ids.txt
        label.text = "This text is displayed after pressing button"

    def build(self):
        return Builder.load_file("styles/button.kv")

if __name__ == '__main__':
    ButtonApp().run()