"""
Lists are used to store MULTIPLE items in a single variable
Think of the like a "BOX" that can hold many items at once
Lists are created with squared brackets []
"""

my_list = [10, 20, 30, 40, 50]
print(my_list)

# Mixed List
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing items by INDEX
# (Indexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])

# You can also use a NEGATIVE index to count in reverse
print(fruits[-1])

# SLICING in a list
#Slicing lets you grab a RANNGE of items using [start:stop]
# it includes "start" but stops BEFORE "stop"

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(numbers[2:5])
print(numbers[:4])
print(numbers[:6])
print(numbers[:-3])
print(numbers[::2]) # [START:STOP:STEP] (STEP = skip over)

# MODIFYING lists items
fruits[1] = "mango"
print(fruits)


# ADDING item
fruits.append("orange") # Adds ONE item to the END of a list
print(fruits)

fruits.insert(1, "Kiwi")
print(fruits)

fruits.extend(["grape", "pear"])
print(fruits)

# REMOVING items
fruits.remove("apple") # Removes by Value (first exact match)
print(fruits)          #Error if item is not in list

fruits.pop(3)           # Removes the LAST item in list
print(fruits)

#fruits.clear()          # Clears the full list
print(fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)

    #CHECK if item exists
    if "mango" in fruits:
        print("mango is in the list")

        # List Length
        print(len(fruits)) # Number if items in list

"""-------------------------------
MINI CHALLENGE: THE GROCERY LIST
-------------------------------
You're building a grocery list app.
1. Create a list called "groceries" with at least 5 items.
2. Print the first and last item using indexing.
3. Use slicing to print just the first 3 items.
4. Add "eggs" to the end of the list using append().
5. Insert "milk" at the very beginning of the list.
6. Remove one item using remove().
7. Check if "bread" is in the list — print a message either way.
8. Print how many items are in the final list.
"""

groceries_list = ["eggs", "bacon", "sasauge", "bread", "butter"]
print(groceries_list)
print(groceries_list[0])
print(groceries_list[4])
print(groceries_list[:3])



