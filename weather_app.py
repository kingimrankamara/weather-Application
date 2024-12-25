import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        result = (f"City: {city}\n"
                  f"Temperature: {main['temp']}°C\n"
                  f"Humidity: {main['humidity']}%\n"
                  f"Pressure: {main['pressure']} hPa\n"
                  f"Weather Description: {weather_description.capitalize()}\n"
                  f"Wind Speed: {wind['speed']} m/s")
        
        return result
    else:
        return "Error fetching the weather data."

def show_weather():
    city = city_entry.get()
    api_key = "your_openweathermap_api_key"
    weather = get_weather(api_key, city)
    messagebox.showinfo("Weather Info", weather)

# Create the GUI
app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter city:").pack(pady=10)
city_entry = tk.Entry(app)
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=show_weather).pack(pady=20)

app.mainloop()
