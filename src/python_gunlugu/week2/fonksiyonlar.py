
import random

def main():

    print(sayi_basamaklarini_topla(12345))  # Örnek kullanım
    print(listenin_ortalamasini_hesapla([1, 2, 3, 4, 5]))  # Örnek kullanım
    dakika, saniye =dakika_ve_saniye_hesapla(125)
    print(f"Dakika : {dakika}, Saniye : {saniye}")  # Örnek kullanım
    print(kelime_sayisini_bul("Merhaba dünya!"))  # Örnek kullanım
            
    print(kelimeyi_ters_cevir("Python"))  # Örnek kullanım
    print(on_tane_rastgele_sayi_uret())  # Örnek kullanım

def sayi_basamaklarini_topla(sayi):
    """ Verilen sayının basamaklarını toplar ve döndürür. """
    toplam = 0
    for basamak in str(sayi):
        toplam += int(basamak)
    return toplam

def listenin_ortalamasini_hesapla(liste):
    """ Verilen listenin ortalamasını hesaplar ve döndürür. """
    if len(liste) == 0:
        return 0
    return sum(liste) / len(liste)

def dakika_ve_saniye_hesapla(toplam_saniye):
    """ Verilen toplam saniyeyi dakika ve saniye cinsine çevirir ve döndürür. """
    dakika = toplam_saniye // 60
    saniye = toplam_saniye % 60
    return dakika, saniye
def kelime_sayisini_bul(metin): 
    """ Verilen metindeki kelime sayısını döndürür. """
    kelimeler = metin.split()
    return len(kelimeler)


def kelimeyi_ters_cevir(kelime):
    """ Verilen kelimeyi ters çevirir ve döndürür. """
    kelime_listesi = list(kelime)
    kelime_listesi.reverse()
    return ''.join(kelime_listesi)  

def on_tane_rastgele_sayi_uret():
    """ 0 ile 100 arasında on tane rastgele sayı üretir ve döndürür. """
    sonuc = []
    for _ in range(10):
        sonuc.append(random.randint(0, 100))
    return sonuc
    

main()
