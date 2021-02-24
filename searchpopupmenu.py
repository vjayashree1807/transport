from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest #can also use requests, see test.py
from kivy.app import App
import certifi
from kivy.clock import Clock
# For snackbar
import requests,json
from kivy.uix.button import Button
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.metrics import dp
 
class SearchPopupMenu(MDInputDialog):
     

    title = 'Search by Address'
    text_button_ok = 'Search'
    def __init__(self): 
        super().__init__() # super() inherits all the methods in MDInputDialog, within the __init__() function
        self.size_hint = [.9, .3]
        self.events_callback = self.callback #call the callback function below
 
    def open(self):
        super().open() # super() inherits all the methods in MDInputDialog, within the open() function
        Clock.schedule_once(self.set_field_focus, 0.5)
 
    def callback(self, *args):
        address = self.text_field.text
        print(address)
        basic_URL = "http://api.openweathermap.org/data/2.5/weather?"
        api_key="30cf19c055b7c5a3e92ba19ec7899c96"
        URL=basic_URL+"APPID="+api_key+"&q="+address
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
        # getting data in the json format
            data = response.json()
        # getting the main dict block
            main = data['main']
            coord=data['coord']
            # getting temperature
            lat=coord['lat']
            lon=coord['lon']
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            #print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {report[0]['description']}")
        else:
            # showing the error message
            print("Error in the HTTP request")
        self.text_field.text=" "
        self.geocode_get_lat_lon(address)

 
    def geocode_get_lat_lon(self, address):
        api_key = "9zMuUUhiyqBsncoYeJrF7jk-NpPUPlxBArB3C8xbe6k"
        address = parse.quote(address)
        url ="https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&apiKey=%s"%(address,api_key)
       
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())
        

    def success(self, urlrequest, result):
        print("Success")
        print(result)
        try:
            latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
            longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
            print(latitude, longitude)
            app = App.get_running_app()
            mapview = app.root.ids.home_screen.ids.mapview
            mapview.center_on(latitude, longitude)
        except:
            Snackbar(text="Address not found, please try other addresses.", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (dp(10) * 2)) / Window.width).open()
            pass
 
 
    def error(self, urlrequest, result):
        print("Error")
        print(result)
 
    def failure(self, urlrequest, result):
        print("Failure")
        print(result)