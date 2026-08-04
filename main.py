import json
import os
from datetime import date

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Android Sensör Erişimi (Plyer)
try:
    from plyer import accelerometer
    from android.permissions import request_permissions, Permission
    ANDROID = True
except ImportError:
    ANDROID = False

DATA_FILE = "step_data.json"
CALORIES_PER_STEP = 0.04  # Adım başına ortalama yakılan kalori (kcal)

def default_data():
    return {
        "date": str(date.today()),
        "steps": 0,
        "goal": 10000,
        "record": 0
    }

def load_data():
    if not os.path.exists(DATA_FILE):
        return default_data()
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        if data.get("date") != str(date.today()):
            if data.get("steps", 0) > data.get("record", 0):
                data["record"] = data["steps"]
            data["date"] = str(date.today())
            data["steps"] = 0
        return data
    except Exception:
        return default_data()

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.08, 0.09, 0.13, 1)
            self.bg = RoundedRectangle(radius=[dp(20)])
        self.bind(pos=self.update, size=self.update)

    def update(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

class StepCounter(App):
    def build(self):
        self.title = "Step Pro"
        self.data = load_data()
        self.steps = self.data.get("steps", 0)
        self.goal = self.data.get("goal", 10000)
        self.record = self.data.get("record", 0)

        self.last_accel = 0
        self.threshold = 11.5  # Sensör adım algılama eşiği

        if ANDROID:
            request_permissions([
                Permission.ACTIVITY_RECOGNITION,
                Permission.HIGH_SAMPLING_RATE_SENSORS
            ])

        root = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(15))

        # Başlık
        self.title_label = Label(
            text="👟 STEP PRO",
            font_size=dp(28),
            bold=True,
            size_hint_y=None,
            height=dp(50)
        )
        root.add_widget(self.title_label)

        # Durum Bilgisi
        self.status = Label(
            text="Sensör Bekleniyor...",
            color=(0.3, 0.7, 1, 1),
            size_hint_y=None,
            height=dp(30)
        )
        root.add_widget(self.status)

        # Adım Sayısı Kartı
        step_card = Card(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        self.step_label = Label(
            text=f"{self.steps}",
            font_size=dp(56),
            bold=True,
            color=(0.2, 0.8, 1, 1)
        )
        self.info_label = Label(
            text=f"Hedef: {self.goal}  |  Rekor: {self.record}",
            font_size=dp(14),
            color=(0.7, 0.7, 0.7, 1)
        )
        step_card.add_widget(self.step_label)
        step_card.add_widget(self.info_label)
        root.add_widget(step_card)

        # Kalori Gösterge Kartı
        calories_burned = round(self.steps * CALORIES_PER_STEP, 1)
        cal_card = Card(orientation="vertical", padding=dp(15), spacing=dp(5))
        
        self.cal_label = Label(
            text=f"🔥 {calories_burned} kcal",
            font_size=dp(32),
            bold=True,
            color=(1, 0.5, 0.2, 1)
        )
        cal_sub_label = Label(
            text="Yakılan Kalori",
            font_size=dp(13),
            color=(0.6, 0.6, 0.6, 1)
        )
        cal_card.add_widget(self.cal_label)
        cal_card.add_widget(cal_sub_label)
        root.add_widget(cal_card)

        # Sensörü Başlat
        self.start_sensor()

        return root

    def start_sensor(self):
        if ANDROID:
            try:
                accelerometer.enable()
                Clock.schedule_interval(self.check_sensor, 1 / 20)
                self.status.text = "Sensör Aktif (Adım Sayılıyor)"
            except Exception as e:
                self.status.text = f"Sensör Başlatılamadı: {e}"
        else:
            self.status.text = "Masaüstü Modu (Sensör Devre Dışı)"

    def check_sensor(self, dt):
        if not ANDROID:
            return
        try:
            val = accelerometer.acceleration
            if val and val[0] is not None:
                accel_magnitude = (val[0]**2 + val[1]**2 + val[2]**2) ** 0.5
                
                if accel_magnitude > self.threshold and self.last_accel <= self.threshold:
                    self.steps += 1
                    self.update_ui()
                
                self.last_accel = accel_magnitude
        except Exception:
            pass

    def update_ui(self):
        # Ekran Elemanlarını Güncelle
        self.step_label.text = f"{self.steps}"
        
        calories_burned = round(self.steps * CALORIES_PER_STEP, 1)
        self.cal_label.text = f"🔥 {calories_burned} kcal"

        if self.steps > self.record:
            self.record = self.steps
            self.info_label.text = f"Hedef: {self.goal}  |  Rekor: {self.record}"
        
        # Verileri Kaydet
        self.data["steps"] = self.steps
        self.data["record"] = self.record
        save_data(self.data)

    def on_stop(self):
        if ANDROID:
            try:
                accelerometer.disable()
            except Exception:
                pass

if __name__ == "__main__":
    StepCounter().run()
