import requests
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.clock import Clock
from datetime import datetime

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(16)
    padding: dp(16)
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        id: digital_clock_label
        text: app.current_time
        font_style: 'H2'
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # White text color

    MDRaisedButton:
        text: "Start Clock"
        on_release: app.start_clock()
        theme_text_color: "Primary"

    MDRaisedButton:
        text: "Stop Clock"
        on_release: app.stop_clock()
        theme_text_color: "Error"

    MDRaisedButton:
        text: "Reset Clock"
        on_release: app.reset_clock()
        theme_text_color: "Primary"

    MDLabel:
        id: date_label
        text: app.current_date
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # White text color

    MDLabel:
        id: day_label
        text: app.current_day
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # White text color

    MDRaisedButton:
        text: "Get Weather"
        on_release: app.get_weather()
        theme_text_color: "Primary"
    MDLabel:
        id: weather_label
        text: app.weather
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1  # White text color
'''

class StyledClockApp(MDApp):
    current_time = StringProperty("")
    current_date = StringProperty("")
    current_day = StringProperty("")
    weather = StringProperty("Weather: N/A")

    def build(self):
        return Builder.load_string(KV)

    def update_time(self, interval):
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%Y-%m-%d")
        self.current_day = now.strftime("%A")

    def start_clock(self):
        self.update_time(0)
        self.clock_event = Clock.schedule_interval(self.update_time, 1)

    def stop_clock(self):
        self.clock_event.cancel()

    def reset_clock(self):
        self.current_time = ""
        self.current_date = ""
        self.current_day = ""

    def get_weather(self):
        # Replace with actual weather data retrieval using an API
        # For simplicity, we set a placeholder value
        self.weather = "Weather: Sunny, 25°C"

if __name__ == '__main__':
    StyledClockApp().run()
