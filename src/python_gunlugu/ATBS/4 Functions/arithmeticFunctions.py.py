def add_one(number):
    """Return the input number plus one."""
    return number + 1

def add_two_numbers(num1, num2):
    """Return the sum of two numbers."""
    for i in range(num2):
        num1 = add_one(num1)

    return num1

def multiply_two_numbers(num1, num2):
    """Return the product of two numbers."""
    product = 0
    for i in range(num2):
        product = add_two_numbers(product, num1)

    return product

while True:
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        result = multiply_two_numbers(first_number, second_number)
        print(f"The product of {first_number} and {second_number} is: {result}")
    except ValueError:
        print("Please enter valid integers for both numbers.")