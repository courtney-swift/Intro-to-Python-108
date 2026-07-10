# Tuples are similar to lists
# BUT! Tuples are IMMUTALE (you cannot change them after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# ACCESSING ITEM
print(my_tuple[0])
print(my_tuple[-2])

#LENGTH of tuple
print(len(my_tuple[-2]))

# NESTED TUPLES
tuple1 = ("a" "b", "c")
tuple2 = (1, 2, 3)

combine = (tuple1, tuple2)
print(combine)
print(tuple1,tuple2)

# SINGLE item Tuples
# you must add a comma at the end or PYTHON wont recognize it as a tuple
single = ("water",)
print(type(single)) # this is a tuple
not_tuple = ("air") # no comma, not a tuple
print(type(not_tuple))


# COUNT and INDEX

letter = ("a", "b", "a", "c", "a")
print(letter.count("a")) # COUNT how many times "a" appears -> 3
print(letter.index("c")) # The indez where "c" first apperars -> 3


# TUPLE UNPACKING
# You can "unpack" a tuple items directly into separate variables

coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

person = ("Courtney", 36, "Student")
name, age, job = person
print(f"MY name is {name} and I am {age} and my job is {job}")

#You are analyzing quiz scores stored in a tuple.
#Create a tuple called "quiz_scores" with at least 6 integer scores.
#Print the FIRST 3 scores and the LAST 3 scores using slicing.
#Print the HIGHEST and LOWEST score using built-in functions.
#Check if ANY score is below 70:
#If yes, print "Warning: At least one failing score!"
#Otherwise print "All students passed!"
#Create a new tuple called "bonus_scores" where each score is increased by 5.
#Combine "quiz_scores" and "bonus_scores" into a tuple called "final_scores".
#Print the total number of scores in "final_scores".
#Print the LAST score in "final_scores".




# Create a tuple with at least 6 integer quiz scores
quiz_scores = (85, 92, 68, 74, 88, 95)

# Print the first 3 scores using slicing
print("First 3 scores:", quiz_scores[:3])

# Print the last 3 scores using slicing
print("Last 3 scores:", quiz_scores[-3:])

# Print the highest and lowest scores
print("Highest score:", max(quiz_scores))
print("Lowest score:", min(quiz_scores))

# Check if any score is below 70
if any(score < 70 for score in quiz_scores):
    print("Warning: At least one failing score!")
else:
    print("All students passed!")

# Create a new tuple with each score increased by 5
bonus_scores = tuple(score + 5 for score in quiz_scores)

# Combine the original and bonus score tuples
final_scores = quiz_scores + bonus_scores

# Print the total number of scores in the combined tuple
print("Total number of scores in final_scores:", len(final_scores))

# Print the last score in the combined tuple
print("Last score in final_scores:", final_scores[-1])



