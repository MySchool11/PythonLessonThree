import test
__author__ = "Samuel Bancroft"
print('''All variables in Python must star with a letter (upper or 
lower case) or an underscore. you cannot use a number at the start
or special characters anywhere in the name''')
print()
print('''valid names include:
_hello, _Hello, hello_world, Hello_world, _123, _a1, a123
invalid names include:
!hello, 123, $help, **123, _!help, _%^test, _help%''')
print()
print('''Another thing to remember is case sensitivity,
so Hello is different from hello''')
print()
print("Try it out, enter a variable name and see if it is valid:")
checkName = "blank"
while checkName:
    checkName = input("press enter on its own when you are finished: ")
    if checkName:
        test.check(checkName)
