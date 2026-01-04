'''
    Q4
    . Create a Python dictionary of 3 cities and their populations. Save it to
    "cities.json".
    1. Then load the JSON and print each city and its population.
    2.Ask the user for a new city & its population - update this info in the json
    file.
'''
import json

cities={
    "Lucknow":5000000,
    "Hardoi":3000000,
    "Hyderabad":9800000 
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

with open("cities.json", "r") as f:
    data = json.load(f)

print("\n--- City Populations ---")
for city, pop in data.items():
    print(f"{city}: {pop}")

new_city = input("\nEnter new city name: ")
new_pop = int(input("Enter its population: "))

data[new_city] = new_pop

with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)