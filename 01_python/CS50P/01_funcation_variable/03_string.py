# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the beginning and end
name = name.strip()

# Capitalize the first character
name = name.capitalize()

# Capitalize the first letter of each word
name = name.title()

# Remove whitespace and capitalize each word
name = name.strip().title()

# Split the name into separate words
first, last = name.split()

# Say hello to the user
print(f"Hello, {name}")

print(f"Hello, {first}")


# String methods
# .strip()      → Removes whitespace from the beginning and end of a string
# .capitalize() → Capitalizes the first character of a string
# .title()      → Capitalizes the first letter of each word in a string
# .split()      → Splits a string into separate parts and returns them as a list

# Method → A function that belongs to an object and performs an action on it
# Examples → name.strip(), name.capitalize(), name.title(), name.split()