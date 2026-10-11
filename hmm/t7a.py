def weather_expert_system(t, h, w):
    if w >= 50:
        return "Stormy Weather"
    if h >= 80 and 20 <= t <= 35:
        return "Rainy Weather"
    if t >= 35:
        return "Hot Weather"
    if t < 20:
        return "Cold Weather"
    if 25 <= t < 35 and h < 60:
        return "Pleasant Weather"
    if 20 <= t < 35 and 60 <= h < 80:
        return "Cloudy Weather"
    return "Moderate Weather"

print("=" * 35 + "\n       WEATHER EXPERT SYSTEM\n" + "=" * 35)
t = float(input("Enter temperature (°C): "))
h = float(input("Enter humidity (%): "))
w = float(input("Enter wind speed (km/h): "))
print("\nWeather Classification:", weather_expert_system(t, h, w))