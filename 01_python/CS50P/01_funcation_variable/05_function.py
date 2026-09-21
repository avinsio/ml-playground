def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()


# Scope
# Scope → The area of a program where a variable can be accessed.
#
# Local variable → A variable created inside a function.
# It can normally be accessed only inside that function.
#
# Global variable → A variable created outside a function.
# It can be accessed by functions in the program.


# Example of local scope
def main():
    name = "Avi"
    print(name)       # Works

# print(name)         # Error: name is local to main()


# Function parameter
# A parameter is a variable that receives a value when a function is called.
#
# Example:
# hello(name)
#     ↓
# def hello(to):
#     ↓
# to receives the value of name


# Default parameter
# A default parameter has a value that is used when no argument is provided.
#
# def hello(to="world"):
#
# hello("Avi")  → hello, Avi
# hello()       → hello, world