import requests

def getWeather(city):
    api_key = "f06e9931e7fd434b1ee815f6f962fd22"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params= {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def display_weather(data):

    if data:
        city_name = data["name"]
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"city: {city_name}")
        print(f"Weather: {weather.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print("ERROR: Unable to fetch weather data: Please check the city or API key")

if __name__ == "__main__":
    print("Welcome to the Weather Forecast App!")
    city = input("Enter the name of the city: ")
    weather_data = getWeather(city)
    display_weather(weather_data)
