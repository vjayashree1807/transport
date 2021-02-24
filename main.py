from kivymd.app import MDApp
from homemapview import HomeMapView
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition,ScreenManager
from searchpopupmenu import SearchPopupMenu
from homegpshelper import HomeGpsHelper
from tata.tatabackdroplayout import TataBackDropLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivy.uix.button import Button
from kivymd.uix.list import MDList
import os
import kivy.properties as kyprops
Window.size = (450,650)


class HomeScreen(Screen):
    pass

class TataScreen(Screen):
    pass
class RouteScreen(Screen):
    pass


class MainApp(MDApp):
    
    current_lat=13.0700
    current_lon=80.2492

    
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass
    
    if os.path.isfile("profile_source.txt"):
        with open("profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "profile.jpg"
    else:
        img_source_path = "profile.jpg"

    
    search_menu = None
    
  
   
  
    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"
        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()
        HomeGpsHelper().run()
        # Instantiate the tat back drop
        self.tata_backdroplayout = TataBackDropLayout().run()
        #Add tata back drop to the tata screen
        self.root.ids.tata_screen.ids.tatabackdrop.add_widget(self.tata_backdroplayout)
        
       
        



    def change_screen(self, screen_name, direction='forward', mode = ""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
    
        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return
 
        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name
 
        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Surge"    
        if screen_name == "tata_screen":
            self.root.ids.titlename.title = "facilites"
        if screen_name=="route_screen":
            self.root.ids.titlename.title = "Route"
            self.root.ids.tata_screen.ids.tatatoolbar.ids.label_title.font_size = '13sp'
           
            
            
MainApp().run()