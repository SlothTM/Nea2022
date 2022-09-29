#imports

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
import sqlite3 
from MainGame import *

#Changes background depending on .x (borderless/fullscreen)
Window.borderless = True

#Causes music to start at the first instance possible using the clock 
def bard(dt):
    music = SoundLoader.load("MenuMusic.wav")
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

kv = Builder.load_file('Menu.kv')

class App(App): #main class for the menu

    def zelda(self):
        link()

    def build(self):
    #creating the database
        logs = sqlite3.connect("User_Logs.db")
    #create a cursor
        c = logs.cursor()

    #Create A table
        c.execute("""CREATE TABLE if not exists details(
            username text
            )""")
    #close and submits changes
        logs.commit()
        logs.close()

        return kv

    #submit function
    def submit(self):

    #creating the database
        logs = sqlite3.connect("User_Logs.db")
        
    #create a cursor
        c = logs.cursor()

    #add to database
        c.execute("INSERT INTO details VALUES (:u_name)",
            {
                'u_name':self.root.ids.user_reg.text,
            })

    #close and submits changes
        logs.commit()
        logs.close()



App().run() #run