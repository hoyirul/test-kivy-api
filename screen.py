import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

Builder.load_file('styles/screen.kv')

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name ="screen_one"))
# screen_manager.add_widget(ScreenTwo(name ="screen_two"))
# screen_manager.add_widget(ScreenThree(name ="screen_three"))

class Main(MDApp):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    Main().run()