"""
A function is a block of code that only runs when its called.
We can pass data to function (parameters), and they can return data as a result. 

def function_name(parameters):
    # Code block (indented)
    # Preform actions using the parameters
    return value # Optional
"""

# SIMPLE function without PARAMETERS
def my_function():
    print("This is my function")

# calling the function
my_function()
    

# function with PARAMETERS
# Patameters allow us to pass information into a function

def print_full_name(fname, lname):
    print(f"The name is: {fname} {lname}")

print_full_name("Courtney", "Swift")

# functions that RETURN Values
# Instead of just printing, functions can send back (return) data

def get_full_name(fname, lname):
    return f"{fname} {lname}" # sends back the full name as text

# Store the returned value in a variable
full_name = get_full_name("Court", "Dez")
print(full_name)

#functions with DEFAULT parameters
# A default parameter means the function will use that value
# if no argument is provided when calling function

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the class.")

    # calling with no argument -> use the default
    greet()

    # calling with argument -> overrides the default
    greet("Courtney")

    # KEYWORD ARGUMENTS
    def describe_pet(name, animal_type, age):
        print(f"{name} is a {age}-years-old {animal_type}.")

        describe_pet("Simba", "Swift", 2) # positional - order matters
        describe_pet(animal_type="dog", name="Simba, age=2 ") # keyword - order doesnt matter


"""
-------------------------------
MINI CHALLENGE: MOVIE TICKET PRICE
-------------------------------
Create a function called calculate_ticket_price().
1. The function should accept:
    age
    is_student (default value = False)
2. Ticket pricing rules:
    Under 13 years old → $8
    13 to 64 years old → $12
    65 and older → $10
3, If is_student is True,
    subtract $2 from the ticket price.
4. Return the final ticket price.
5. Call the function twice:
    One regular customer
    One student
6. Print the returned prices.
"""   


# SOLUTION

# MINI CHALLENGE: MOVIE TICKET PRICE
def calculate_ticket_price(age, is_student=False): # 1. Function accepts age + is_student
    # 2. Base pricing rules
    if age < 13:  # 13- ==> $8
        price = 8
    elif 13 <= age <= 64:  # age 13-64 ==> $12
        price = 12
    else:  # age 65+ ==> $10
        price = 10
    if is_student:  # 3. Student discount
        price -= 2
    return price
regular_customer_price = calculate_ticket_price(30)  # 5. Call the function twice: 1x regular adult & 1x student
student_price = calculate_ticket_price(19, is_student=True) 

print("Regular customer price:", regular_customer_price)  # 6. Print both returned prices
print("Student price:", student_price)





