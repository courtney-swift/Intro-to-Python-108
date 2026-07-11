"""
A for loop in python is a control structure that lets you repeat a block of code
in a sequence (list, string, tuple, set, or any range of numbers)

It is used when you know how many times you want to repeat an action or process each element in a collection

for variable in sequence:
    # Code block runs for each item in a sequence
"""


# Loop through a List
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)

    print("-------------------------------")

# loop through a string
for letter in "Hello":
    print(letter)

    print("-------------------------------")

    # range() generates a sequence of numbers

    for x in range(5): # stops at index 5
        print(x)      # prints 0-4

    print("-------------------------------")


    # start and stop range()
    for x in range(2, 6):
        print(x)

    print("-------------------------------")

    # start,stop,step
    for number in range(0, 10, 2):
        print(number)

    print("-------------------------------")

    # ELSE in for loop
    for x in range(3):
        print(x)
    else: # run when the loop is done
        print("loop is finished")

        #BREAK and CONTINUE in for loops
        for x in range(10):
            if x == 5: # if- condition check
                continue # Skip 5 to continue to next iteration 
            if x == 8:  # 8 in the index = 7
                break # STOP loop completely
            print(x)

print("-------------------------------")

#ENUMERATE() get the index AND the value

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit) # 0 apple, 1 banana, 2 cherry

    # You can choose where the counting start
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")

print("-------------------------------")


# ZIP() loop through two lists together

names = ["Courtney", "Chiaki", "Anela"]
scores =[98, 95, 99]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# NESTED for loops

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print() # moves to a new line after each row finishes

print("-------------------------------")


"""
MINI CHALLENGE
1. Ask the user to enter a number and store it in a variable called num.
2. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10)
3. Inside the loop, multiply num by the current loop value (1)
"""

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Repeat 10 times (1 through 10)
for numbs in range(1, 11):
    # Multiply the user's number by the current loop value
    result = num * numbs

    # Display the multiplication
    print(f"{num} x {numbs} = {result}")