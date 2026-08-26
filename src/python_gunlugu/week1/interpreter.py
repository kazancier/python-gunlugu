def main():
    expression = input("Expression: ")
    x, operator, y = expression.split()
    x = float(x)
    y = float(y)
    match operator:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
        case "/":
            result = x / y

    result = round(result,1)
    print(result)


main()