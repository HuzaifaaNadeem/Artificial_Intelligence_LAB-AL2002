print("Traffic Light Reflex Agent")
print()

trafficConditions = ["Heavy Traffic", "Light Traffic"]

for condition in trafficConditions:
    if condition == "Heavy Traffic":
        print("Percept: Heavy Traffic → Action: Extend Green Time")
    else:
        print("Percept: Light Traffic → Action: Normal Green")
