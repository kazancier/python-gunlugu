print("Enter C or F to indicate Celsius or Fahrenheit: ")
scale = input()
print("Enter the number of degrees:")
degrees= int(input())

if (scale.strip().lower() == "c" and (degrees < 16 or degrees >38)) or (scale.strip().lower() == "f" and (degrees < 60.8 or degrees > 100.4)) :
    print("Danger")
else:
    print("Safe")