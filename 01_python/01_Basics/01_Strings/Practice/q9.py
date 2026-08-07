'''
# String Concatenation

Take first name and last name separately.
Print:
    - Hello, Avi Sharma!
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

message = "Hello, {} {}!".format(first_name, last_name)
print(message)