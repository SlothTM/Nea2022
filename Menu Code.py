#imports from different modules

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.textinput import TextInput


class Menu(Screen):
    pass

class Login(Screen):
    pass

class Menu_Manager(ScreenManager):
    pass



kv = Builder.load_file('Menu.kv')

class App(App): #main class for the menu
    def build(self):
        return kv


App().run()
