import time

def main():
    while True:
        try:
            user_input = int(input("Enter a number to see 'Tick' and 'Tock': "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        tick_tock(user_input)

def tick_tock(sayi):
    """This function prints "Tick" and "Tock" alternately 
    for the number of times specified by the user."""
    for i in range(sayi):
        if i % 2 == 0:  
            print("Tick")
            time.sleep(1)  # Wait for 1 second
        else:       
            print("Tock")
            time.sleep(1)  # Wait for 1 second

main()