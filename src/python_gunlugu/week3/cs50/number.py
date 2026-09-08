
def main():

    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()

"""
while True:
    try:
        x = int(input("What's x? "))
        
    except ValueError:
        print("x is not an integer")

    else:
        break

print(f"x is {x}")

"""
"""

try:
    x = int(input("What's x? "))
    
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

"""