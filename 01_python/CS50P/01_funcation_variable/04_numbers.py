# Integers (int)

# int → Whole numbers, including positive, negative, and zero
# Examples → -2, -1, 0, 1, 2

# Common arithmetic operators
# +  → Addition
# -  → Subtraction
# *  → Multiplication
# /  → Division
# %  → Modulus (remainder)

# Calculator

x = int(input("What's x? "))
y = int(input("What's y? "))

# Addition
print(x + y)


# input() always returns a string
# Typecasting → Converting a value from one data type to another
# Examples → int(), float(), str()

# "Hello" + "World" → "HelloWorld"
# String + String → Concatenation

# Float


x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(f"{z:,}")


# round(number[, ndigits])
#
# number  → The number you want to round
# ndigits → Number of decimal places to keep (optional)
#
# [] → The argument is optional
#
# Example:
# round(3.14159, 2) → 3.14
# round(3.14159)    → 3


# f"{z:,}" → Formats a number with commas
#
# Example:
# z = 1000000
# f"{z:,}" → "1,000,000"


# Division

z = x / y

# Round to 2 decimal places
print(round(z, 2))

# Format to exactly 2 decimal places
print(f"{z:.2f}")