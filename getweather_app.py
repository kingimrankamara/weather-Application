import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Error fetching the weather data.")

if __name__ == "__main__":
    api_key = "your_openweathermap_api_key"
    city = input("Enter the city name: ")
    get_weather(api_key, city)
