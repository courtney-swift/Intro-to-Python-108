# Create a dictionary about a plant
car = {
    "name": "Hellcat",
    "type": "Coupe",
    "location": "Garage",
    "washing": "Every 1 weeks"
}

print("Original dictionary:", car)
print("Dictionary length:", len(car))

# Access values using keys
print("car name:", car["name"])
print("Location:", car["location"])

# Add a new key
car["status"] = "waxed"
print("After adding status:", car)
print("Dictionary length:", len(car))

# Update an existing value
car["location"] = "Driveway"
print("After updating location:", car)
print("Dictionary length:", len(car))

# Remove a key
car.pop("status")
print("After removing status:", car)
print("Dictionary length:", len(car))

# Loop through the dictionary
print("\ncar Information:")
for key, value in car.items():
    print(f"{key}: {value}")



