import requests

API_KEY = "c5a3a0cc394770ec4985b0a807aa29ae"


def get_weather(city):
    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        print("❌ ERROR: Please add your OpenWeatherMap API key in the code!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Print full message in case of error
    if data.get("cod") != 200:
        print("\n❌ ERROR:", data.get("message", "Unknown error"))
        return

    # Extract data
    name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    # Print weather
    print("\n===== WEATHER REPORT =====")
    print("City:", name)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", desc)


# ===== MAIN PROGRAM =====
city_name = input("Enter city name: ")
get_weather(city_name)
