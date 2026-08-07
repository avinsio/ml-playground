"""
# Find a Word

Ask the user for a sentence.
Find the position of "Python".
If it doesn't exist, print:
                     - Python not found 

"""

message = input("Enter a sentence: ")

position = message.lower().find("python")

if position != -1:
    print(position)
else:
    print("Python not found")