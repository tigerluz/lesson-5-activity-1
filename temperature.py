temperature = int(input("Enter todays temperature in Celsius; "))
if temperature < 20:

    outfit = "jacket"
    print("It is cold today")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today. ")
    print("Wear a", outfit)

    is_raining = input("Is it raining today? (yes/no)")

    if is_raining == "yes":
        print("Bring an umbrella")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    needs_windbreaker = "yes"
    shoes = "boots"
    print("The ground is wet.")
    print("Weat", shoes)
else: 
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)
print("")
print("Weather check complete!")
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker needed: ", needs_windbreaker)
print("Shoes Chosen:", shoes)