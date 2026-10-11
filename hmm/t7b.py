def weather(t, h, w):
    if w >= 50:                    return "Stormy", "R1"
    if h >= 80 and 20 <= t <= 35:  return "Rainy", "R2"
    if t >= 35:                    return "Hot", "R3"
    if t < 20:                     return "Cold", "R4"
    if 25 <= t < 35 and h < 60:    return "Pleasant", "R5"
    if 20 <= t < 35 and h >= 60:   return "Cloudy", "R6"
    return "Moderate", "Default"

t = float(input("Enter temperature (°C): "))
h = float(input("Enter humidity (%): "))
w = float(input("Enter wind speed (km/h): "))

result, rule = weather(t, h, w)
print(f"Rule {rule} fired")
print("Final Conclusion:", result, "Weather")