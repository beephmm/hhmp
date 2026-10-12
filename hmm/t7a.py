def weather_expert_system(temperature, humidity, wind_speed):
    if wind_speed >= 50:
        return "Stormy Weather"
    elif humidity >= 80 and 20 <= temperature <= 35:
        return "Rainy Weather"
    elif temperature >= 35:
        return "Hot Weather"
    elif temperature < 20:
        return "Cold Weather"
    elif 25 <= temperature < 35 and humidity < 60:
        return "Pleasant Weather"
    elif 20 <= temperature < 35 and 60 <= humidity < 80:
        return "Cloudy Weather"
    else:
        return "Moderate Weather"

print("===================================")
print("        WEATHER EXPERT SYSTEM")
print("===================================")

temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
wind_speed = float(input("Enter wind speed (km/h): "))

result = weather_expert_system(temperature, humidity, wind_speed)

print("\nWeather Classification:", result)
