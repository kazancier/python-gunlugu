# prompt user for X/Y
# x is non negative integer
# y is positive integer
# output as a percentage rounded to the nearest integer
# if %1 or less output E 
# if %99 or more output F
# if X,Y not integer or X>Y or  Y is 0, prompt again

def main():
    while True:
        try:
            x = int(input("What's X of X/Y?"))
            y = int(input("What's Y of X/Y?"))
        except ValueError:
            print("X and Y must be integers. Please try again.")

        else:
            if x < 0 or y <= 0 or x > y:
                print("Invalid input. Ensure that X is a non-negative integer, Y is a positive integer, and X is not greater than Y.")
            else:
                break        

    percentage = (x / y) * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{round(percentage)}%")

main()