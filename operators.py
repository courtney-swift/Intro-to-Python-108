# ARITHMETIC OPERATORS - used with numeric values to preform common
# math operations 

x = 1
y = 2
res = 0

res = x + y
print(res)
res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res = x ** y
print(res)

res = x // y
print(res)


# ASSIGNMENT OPERATORS - used to assign values to variables
# = means "put this value inside the (variable)"
# +=, -=, *=, /= are shortcuts

x = 5
x += 5
x -= 3
x *= 3
x /= 2
print(x)

# COMPARSION OPERATORS - used to compare two values
# == (equal to), !=(not equal), <=(less than) >=(greater than)

# LOGICAL OPERATERS - used to combine conditoinal statements (booleans T/F)
# and -> both must be true
# or -> at least one must be true
# not -> flips True to False (vice versa)

x = 3
y = 10
z = 10

print(x == y and y == z) #False, because conditions are NOT true
print(x == y or y == z) # True because one condition is true
print(not x == y )      # True, because x != y

# MEMBERSHIP OPERATOR - used to test if a squence is presented in an object
# in -> check is something is inside a sequence (list, string. etc)
# not in -> checks if something is NOT in a sequence

x = [1, 2, 3, 4, 5]

print(4 in x)
print(9 not in x)

