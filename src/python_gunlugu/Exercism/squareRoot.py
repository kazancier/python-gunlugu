num = int(input("Write the number you want to learn the square root: "))
i=0
while i < num :
    if num >= i**2 and num < (i+1)**2 :
        print (f"{num}'un karekökü {i}")
        break
    else:
        i += 1
        