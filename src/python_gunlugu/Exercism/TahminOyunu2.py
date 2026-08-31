import random

devam_ediyor = True
rand_num = random.randint(0,100)
while devam_ediyor:
    # inputu ans'a kaydet
    ans = input("Guess the number?: ")
    # ans isdigitse num a eğitle devam et
    if ans.isdigit():
        num = int(ans)
    # ans isdigt değilse print(hata tekrar)
        if rand_num == num:
            print(f"Bildin sayı {num}.")
            devam_ediyor = False
        elif rand_num > num:
            print("Çok küçük")
        elif rand_num < num:
            print("Çok büyük")
    else:
        print("Pozitif bir tam sayı girmeniz gerekiyor.")

