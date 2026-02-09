print("Restaurant Selector")
print()

restaurants = {
    "A": {"distance": 3, "rating": 7},
    "B": {"distance": 5, "rating": 9}
}

utilities = {}

for name in restaurants:
    utility = restaurants[name]["rating"] - restaurants[name]["distance"]
    utilities[name] = utility
    print("Restaurant", name, "Utility =", utility)

best_choice = max(utilities, key=utilities.get)
print()
print("Selected Restaurant:", best_choice)
