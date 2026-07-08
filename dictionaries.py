# Dictionaries stores data in KEY: VALUE pairs
# written using curley Brackets {}

student = {
    "name": "Courteny",
    "age": 36,
    "major": "Computer Science"
}

print(student)

# Acessing items
print(student["name"]) # accessing by key
print(student.get("age"))


#ADDING new items
student["graduation_year"] = 2025
print(student)

# CHANGING Values
student["age"] = 23
print(student)

# REMOVING item
student.pop("major") # Remove key "major" and its value
print(student)

# CHECKING if a key exists
if "name" in student:
    print("Key 'name' exists")

    # NESTED dictionaries
    students = {
        "student1": {"name": "Courtney", "age": 36},
        "student2": {"name": "Chiaki", "age": 43}
    }
print(students ["student2"]["name"]) #Access nested value

#LOOPING through a dictionary
# .keys() -> just the key
# .values() -> just the values
# .items() -> key/value pairs together

for key in student.keys():
    print(key)

for values in student.values():
        print(values)

for key, value in student.items():
            print(f"{key} : {value}")

#UPDATING MULTIPLE keys at once 
#update() merges a second dictionary into the first one.
# Existing keys get overwritten, new keys get added
student.update({"age": 25, "gpa": 3.8})

# TIP: highlight code and SHIFT to then wrap it in any bracket you need (), {} ect

"""
 -------------------------------
MINI CHALLENGE: STUDENT REPORT CARD 
-------------------------------
You need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    -"subject"
    -"grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
   If between 70 and 89 → print "Good job!"
   Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""

report_card = {
    "name": "Courtney",
    "subject": "Math",
    "grades": (90, 85, 88)
}
print(report_card["name"])
print(report_card["subject"])
average = sum(report_card["grades"]) / len(report_card["grades"])
report_card["average"] = average
if average >= 90:
    print("Excellent!")
elif 70 <= average <= 89:
    print("Good job!")
else:
    print("Needs improvement!")
report_card.pop("subject")
print(report_card)

