"""
An if-else statement in Python is a conditional control structure that lies you decide which block of code to run depending on wheather a conition is True or False

if condition:
-Code block runs if condition is True

elif another_condition:
-Code block run if first conition is False
-and this condition is True 

else:
Code block runs if none of the above condition are true

if- checks a condition
elif (else if) - checks another condition 
else - runs if all other conditions are False
"""

x = -10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand IF statements
#you can write it all in one line

if x > 5: print("x is greater than 5")

# Short hand IF ... ELSE
print("Even") if x % 2 == 0 else print("odd")

#Nested IF statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

        # Combining conditions

        age = 19

        if age >= 18 and age <=21:
            print("You are betwee 18 and 21 years old")

            """
            MINI CHALLENGE
            1. Ask the user to enter their age and store it in a cariable called age.
            2. Ask the user if they have a valid ID
            (The user should enter "yes" or "no)
            Store the answer in a variable  called has_id
            3. Determine admission rules:
            print "Accesse Granted!"


            """


has_id = input()


User_Age = int (input("Enter your age:"))
age = int(User_Age)
id = (input("Do you have a valid ID? Yes or No:"))
has_id = input()
print(f"Yes {age} {has_id}")

