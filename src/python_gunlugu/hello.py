""" Archive 1

# Ask user for their name
name = input("What's your name? ")
surname = input("What is your surname? ")

#str functions remove whitspace from the string

name = name.strip  ()

name = name.title()

#merge methods

surname = surname.strip().title()

# Say hello to user
print("hello, "+ name, surname, "!")

#parameters
print("Hello, ",end="")
print(name, )
#two double quotes inside
print('"hello"')

#Escaping
print("\"hello\"")

# put variable in curly braces

print(f"hello, {name}")

#best version

name=input("What's your name? ").strip().title()

print(f"Hello, {name}!")


name = input("What's your name? ").strip().title()

first, last = name.split(" ")

print(f"Hello, {first}")


"""

"""

def hello(to="world"):
    print(f"hello, {to}")

hello()
name = input("What's your name? ")
hello(name)

"""

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print(f"hello, {to}")


main()
