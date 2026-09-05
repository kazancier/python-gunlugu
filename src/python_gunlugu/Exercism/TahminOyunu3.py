import random

def main():

   
    rastgele_sayi = rastgele_sayi_uret()
    tahmin = gecerli_tahmin_al()
    while not kiyasla(tahmin, rastgele_sayi):
        tahmin = gecerli_tahmin_al()

    
       
        
def rastgele_sayi_uret():
    """ Sıfır ile 100 arasında rastgele bir sayı üretir ve döndürür. """
    return random.randint(0,100)

def gecerli_tahmin_al():
    """ Kullanıcıdan tahmin alır, tahmin digitse ve pozitifse int olarak döndürür, değilse tekrar sorar. """
    while True:
        tahmin = input("Guess the number?: ")
        if tahmin.isdigit():
            return int(tahmin)
        else:
            print("Lütfen pozitif bir sayı giriniz.")
            
def kiyasla(tahmin, rastgele_sayi):
    """ Tahmin ve rastgele sayıyı karşılaştırır, tahmin doğruysa True döndürür, değilse False döndürür ve kullanıcıya ipucu verir. """
    if tahmin == rastgele_sayi:
        print(f"Bildin sayı {tahmin}.")
        return True
    elif tahmin < rastgele_sayi:
        print("Çok küçük")
        return False
    else:
        print("Çok büyük")
        return False
main()