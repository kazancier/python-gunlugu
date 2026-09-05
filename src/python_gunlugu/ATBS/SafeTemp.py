print("Enter C or F to indicate Celsius or Fahrenheit: ")
scale = input()
print("Enter the number of degrees:")
degrees= int(input())

if scale.lower().strip() == "c":
    if degrees < 16 or degrees >38 :
        print("Danger")
    else:
        print("Safe")
if scale.lower().strip() =="f":
    if degrees < 60.8 or degrees > 100.4 :
        print("Danger")
    else:
        print("Safe") 



        