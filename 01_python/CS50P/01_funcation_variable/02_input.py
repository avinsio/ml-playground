# Ask the user for their name
name = input("What's your name? ")

# Say hello to the user
print("Hello,", name)

print("Hello, ", end="")   # Override the default ending
print(name)

print("Hello,", name, sep="")

# f-string → A formatted string used to insert values directly into a string
print(f"Hello, {name}")

# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

# *objects → Allows multiple values
# sep → Separates multiple values; default is " "
# end → Controls what is printed at the end; default is "\n"

print('Hello, "friend"')
print("Hello, \"friend\"")

# String → A sequence of characters enclosed in quotes
# Quotes → Single (') or double (") quotes can create strings
# Escape character (\) → Used to represent special characters inside a string
# \" → Represents a double quote inside a string
# \' → Represents a single quote inside a string