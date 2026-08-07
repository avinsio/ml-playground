# ========================================
# Strings
# ========================================

# Creating Strings

message = "Hello World"

print(message)


# ========================================
# Length
# ========================================

print(len(message))


# ========================================
# Indexing
# ========================================

print(message[0])     # First character
print(message[-1])    # Last character


# ========================================
# Slicing
# ========================================

print(message[:5])    # Hello
print(message[6:])    # World
print(message[0:5])   # Hello


# ========================================
# String Methods
# ========================================

print(message.lower())
print(message.upper())

print(message.count("l"))

print(message.find("World"))

print(message.replace("World", "Universe"))


# ========================================
# String Concatenation
# ========================================

greeting = "Hello"
name = "Michael"

print(greeting + ", " + name + "!")


# ========================================
# String Formatting
# ========================================

print("{} {}".format(greeting, name))

print(f"{greeting}, {name}")

print(f"{greeting}, {name.upper()}")


# ========================================
# Useful Built-in Functions
# ========================================

print(dir(message))

help(str.lower)