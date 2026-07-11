# Create a list of favorite plants
cars = ["Viper", "Ram", "Hellcat", "Charger"]
print("Original list:", cars)
print("List length:", len(cars))

# Access items by index
print("First car:", cars[0])
print("Third car:", cars[2])

# Replace a value
cars[1] = "Avenger"
print("After replacing Avenger with Ram:", cars)
print("List length:", len(cars))

# Remove an item by value
cars.remove("Avenger")
print("After removing Avenger:", cars)
print("List length:", len(cars))

# Remove an item by index
cars.pop(0)
print("After removing the first car:", cars)
print("List length:", len(cars))