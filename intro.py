print("Hello world from Python!")
print(2)
print(5 + 3)
print(True)

# SHORTCUTS
# ctrl + s
# up arrow key for already used/previous commands

'''
This is multi line comment
triple quotes around your comment
'''


# Variables and concatenation
name = "Courtney"
age = 36
print(name, age)


print("My name is " + name +  "and I am"  + str(age) +  "years old")


pet = "Simba"
job = "IT" 
car = "Skyline"
country = "Japan"
kids = 2

print("My name is" + name + "I live in" + country + ". I have a dog named " + pet + "and I work in" + job + "I drive a" + car + "and I have" + str(kids) +  ".")

# F string
print(f"""My name is {name}.  I live in {country}. I have a dog named {pet} I work in {job} and I drive a {car} and I have {kids} kids.""")

# TYPE FUNCTIONS
print(type(name))
print(type(kids))
print(type(True))

# CASTING (changing data types)
print(20 + int("20"))
print(20 + age)


# INPUT FUNCTION
user_name = int (input("Enter your age:"))
print(f"Hello, {user_name}!")

# ALWAYS RETURNS STRING
# print(type(input("Enter your age:")))

# converting input to int
new_age = int (input("Enter your age:"))
print(user_name + new_age)

slices= int (input("How many pizza slices are there?:"))
people= int (input("how many people are there?:"))
slice_per_person = slices / people
print(f"each person gets {slice_per_person}")