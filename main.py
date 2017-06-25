__author__ = "Mr Bancroft"

import test

print('''All variables in Python must star with a letter (upper or          
lower case) or an underscore. you cannot use a number at the start
or special characters anywhere in the name''')                          # Print information about variables
print()                                                                 # Print blank line
print('''valid names include:
_hello, _Hello, hello_world, Hello_world, _123, _a1, a123
invalid names include:
!hello, 123, $help, **123, _!help, _%^test, _help%''')                  # Print information about variables
print()                                                                 # Print blank line
print('''Another thing to remember is case sensitivity,
so Hello is different from hello''')                                    # Print information about variables
print()                                                                 # Print blank line
print("Try it out, enter a variable name and see if it is valid:")      # Print instructions
checkName = "blank"                                                     # Set checkName string to arbitrary value so initial while check passes
while checkName:                                                        # While checkName uses a boolean check because an empty string is false and a populated one true in Python
    checkName = input("press enter on its own when you are finished: ") # Input the variable name into checkName string
    if checkName:                                                       # Check variable contains something to prevent odd error message when pressing enter alone to exit while loop
        test.check(checkName)                                           # Pass the variable name string to the check() method in the test.py file
