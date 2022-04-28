#imports

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.textinput import TextInput
from random import random

#Menu:
class Menu(Screen): #Menu screen
    pass

class Login(Screen): #Login screen
    pass

class Register(Screen): #Register screen
    pass

class Forgotten(Screen): #Forgotten password screen 
    pass

#Game Menu:
class GameMenu(Screen):
    pass

class Setting(Screen):
    pass

class Menu_Manager(ScreenManager): #manages each screeen allows for changing between the menu screens
    pass


kv = Builder.load_file('Menu.kv')

class App(App): #main class for the menu
    def build(self):
        return kv
        


App().run() #run
