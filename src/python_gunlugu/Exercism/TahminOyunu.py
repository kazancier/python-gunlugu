import random

i = True
rand_num = random.randint(0,100)
while i == True:
    num = int(input("Guess the number?: "))
    if not (isinstance(num,int) and num > 0):
        print("Lütfen pozitif bir tamsayı girin.")
    elif rand_num == int(num):
        print(f"Bildin sayı {num}.")
        i = False
    elif rand_num >= int(num):
        print("Çok küçük")
    elif rand_num <= int(num):
        print("Çok büyük")
    
print("Tebrikler")
