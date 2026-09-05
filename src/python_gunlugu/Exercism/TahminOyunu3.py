"""
1 - geçerli tahmin al fonksiyonunu ve main deki çok küçük/büyükü değiştiririm

2-kiyasla_b 'yi test etmek daha kolay sadece dönenlere bakarım, kıyaslada printlere de bakmak gerekir.

3-kıyasla_b fonsiyon daha kompak oldu
"""

import random

def main():

   
    rastgele_sayi = rastgele_sayi_uret()
    while True:
        tahmin = gecerli_tahmin_al()
        kiyas = kiyasla_b(tahmin,rastgele_sayi)
        if kiyas == "Bildin":
            print(f"Bildin sayı {tahmin}.")
            break
        elif kiyas == "Küçük":
            print("Çok küçük")
        elif kiyas == "Büyük":
            print("Çok büyük")
            

    
       
        
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
 #artık kullanımıyor. kıyasla_b fonksiyonu kullanılıyor.           
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

def kiyasla_b(tahmin,rastgele_sayi):
    """ Tahmin ve rastgele sayıyı karşılaştırır, tahmin doğruysa Bildin döndürür, değilse Küçük / Büyük döndürür . """
    if tahmin == rastgele_sayi:
        return "Bildin"
    elif tahmin < rastgele_sayi:
        return "Küçük"
    else:
        return "Büyük"
main()