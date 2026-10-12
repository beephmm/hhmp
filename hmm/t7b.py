def weather_expert_system(temp, humidity, wind):
    print("\n--- Inference Process ---")

    if wind >= 50:
        print("Rule R1 fired: IF wind speed >= 50 THEN Stormy")
        return "Stormy Weather"
    elif humidity >= 80 and 20 <= temp <= 35:
        print("Rule R2 fired: IF humidity >= 80 AND temperature is 20-35 THEN Rainy")
        return "Rainy Weather"
    elif temp >= 35:
        print("Rule R3 fired: IF temperature >= 35 THEN Hot")
        return "Hot Weather"
    elif temp < 20:
        print("Rule R4 fired: IF temperature < 20 THEN Cold")
        return "Cold Weather"
    elif 25 <= temp < 35 and humidity < 60:
        print("Rule R5 fired: IF temperature is 25-35 AND humidity < 60 THEN Pleasant")
        return "Pleasant Weather"
    elif 20 <= temp < 35 and 60 <= humidity < 80:
        print("Rule R6 fired: IF temperature is 20-35 AND humidity is 60-79 THEN Cloudy")
        return "Cloudy Weather"
    else:
        print("Default rule fired: Moderate Weather")
        return "Moderate Weather"

temp = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
wind = float(input("Enter wind speed (km/h): "))

classification = weather_expert_system(temp, humidity, wind)

print("\nFinal Conclusion:", classification)
