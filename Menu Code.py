#imports

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.textinput import TextInput


class Menu(Screen): #Menu screen
    pass

class Login(Screen): #Login screen
    pass

class Register(Screen): #Register screen
    pass

class Menu_Manager(ScreenManager): #manages each screeen allows for changing between the menu screens
    pass



kv = Builder.load_file('Menu.kv')

class App(App): #main class for the menu
    def build(self):
        return kv


App().run() #run

