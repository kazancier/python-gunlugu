import random

i = True
rand_num = random.randint(0,100)
while i == True:
    num = int(input("Guess the number?: "))
    if num <= 0:
        print("Lütfen pozitif bir sayı girin.")
    elif rand_num == int(num):
        print(f"Bildin sayı {num}.")
        i = False
    elif rand_num >= int(num):
        print("Çok küçük")
    elif rand_num <= int(num):
        print("Çok büyük")
    
print("Tebrikler")
