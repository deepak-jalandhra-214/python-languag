import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")

else:
    print("City not found!")