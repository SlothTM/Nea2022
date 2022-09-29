#imports
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen, NoTransition
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
from random import random
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from random import random
import REG as R
import LOG as L



#Changes background depending on .x (borderless/fullscreen)
Window.borderless = True

#Causes music to start at the first instance possible using the clock 
def bard(dt):
    music = SoundLoader.load("Assets/MenuMusic.wav")
    if music:
        music.play()
        music.loop = True

Clock.schedule_once(bard)

#Menu:
class Menu(Screen):
    pass

#Each screen in the Menu 
class Login(Screen): 
    pass

class Register(Screen):
    pass

class Forgotten(Screen):
    pass

#Game Menu:
class GameMenu(Screen):
    pass

#Each screen in the Game menu

class Setting(Screen):
    pass

class Stats(Screen):
    pass

class Secret(Screen):
    pass

#manages each screeen allows for changing between the menu screens
class Menu_Manager(ScreenManager):
    pass


class App(App): #main class for the menu

    def build(self):
        return Builder.load_file('Menu.kv')

    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()

    def log(self):
        L.call_log()

    def reg(self):
        R.call_reg()

App().run() #run menu


