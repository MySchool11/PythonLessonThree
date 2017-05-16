__author__ = "Samuel Bancroft"
# You can ignore this file if you do not feel able to grasp what is happening here
# If you want to know, read on
def check(stringToCheck):                               # This defines a function call check which needs a string passed to it
    if stringToCheck.isidentifier():                    # If statement checks whether the passed string is a valid variable name using the inbuilt function isidentifier()
        print("Valid variable name in Python 3.x")      # If valid print statement confirming validity
    else:                                               # Else
        print("Invalid variable name in Python 3.x")    # Print statement confirming name is invalid
