def main():
    expression = input("Expression: ")
    if len(expression.split()) != 3:
        print("ifade hatalı tekrar giriniz.")
    else:  
        x, operator, y = expression.split()
        x = float(x)
        y = float(y)
        match operator:
            case "+":
                result = x + y
                print(round(result,1))
            case "-":
                result = x - y
                print(round(result,1))
            case "*":
                result = x * y
                print(round(result,1))
            case "/":
                if y == 0:
                    result = "Bir sayıyı sıfıra bölemezsiniz"
                    print(result)
                else:
                    result = x / y
                    print(round(result,1))
                    
            case _:
                print("Operator tanınmadı.")


main()