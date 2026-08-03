import json
import os
from datetime import date

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp

from kivy.graphics import Color, RoundedRectangle

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


# ===============================
# ANDROID SENSOR
# ===============================

try:
    from android.permissions import request_permissions, Permission
    ANDROID = True

except:
    ANDROID = False



DATA_FILE = "step_data.json"



# ===============================
# VERİLER
# ===============================

def default_data():

    return {
        "date": str(date.today()),
        "steps": 0,
        "goal": 10000,
        "record": 0,
        "sensor_start": None
    }



def load_data():

    if not os.path.exists(DATA_FILE):
        return default_data()


    try:

        with open(DATA_FILE,"r") as f:
            data=json.load(f)


        if data["date"] != str(date.today()):

            if data["steps"] > data["record"]:
                data["record"]=data["steps"]


            data["date"]=str(date.today())
            data["steps"]=0
            data["sensor_start"]=None


        return data


    except:

        return default_data()



def save_data(data):

    with open(DATA_FILE,"w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



# ===============================
# KART TASARIMI
# ===============================

class Card(BoxLayout):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)


        with self.canvas.before:

            Color(
                0.08,
                0.09,
                0.13,
                1
            )


            self.bg = RoundedRectangle(
                radius=[dp(20)]
            )


        self.bind(
            pos=self.update,
            size=self.update
        )



    def update(self,*args):

        self.bg.pos=self.pos
        self.bg.size=self.size



# ===============================
# UYGULAMA
# ===============================


class StepCounter(App):


    def build(self):

        self.title="Step Pro"



        self.data=load_data()


        self.steps=self.data["steps"]
        self.goal=self.data["goal"]
        self.record=self.data["record"]

        self.sensor_start=self.data["sensor_start"]



        if ANDROID:

            request_permissions(
                [
                    Permission.ACTIVITY_RECOGNITION
                ]
            )



        root=BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15)
        )



        with root.canvas.before:

            Color(
                0.03,
                0.04,
                0.06,
                1
            )


            self.background=RoundedRectangle()



        root.bind(
            pos=self.update_bg,
            size=self.update_bg
        )



        title=Label(

            text="👟 STEP PRO",

            font_size=dp(30),

            bold=True,

            size_hint_y=None,

            height=dp(60)

        )


        root.add_widget(title)



        self.status=Label(

            text="Sensör hazırlanıyor",

            color=(0.3,0.7,1,1),

            size_hint_y=None,

            height=dp(30)

        )


        root.add_widget(self.status)
