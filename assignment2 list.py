# Create a list of favorite plants
plants = ["lily", "petunia", "haworthia", "caladium"]
print("Original list:", plants)
print("List length:", len(plants))

# Access items by index
print("First plant:", plants[0])
print("Third plant:", plants[2])

# Replace a value
plants[1] = "pothos"
print("After replacing petunia with pothos:", plants)
print("List length:", len(plants))

# Remove an item by value
plants.remove("caladium")
print("After removing caladium:", plants)
print("List length:", len(plants))

# Remove an item by index
plants.pop(0)
print("After removing the first plant:", plants)
print("List length:", len(plants))