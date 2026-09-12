"""
Şartname :

Programa bir metin verildiğinde bu metinde 
hangi kelimeler kaçar kez geçmiş bunu bir sözlük olarak 
döndürsün.

Büyük harf küçük harf ayrımı yapmasın. Aynı kelimenin
büyük ya da küçük harf yazımlarını aynı görsün.

Çıktıyı ingilizce alfabetik olarak sıralasın.


Örnek :

Yapay zeka teknolojileri hızla gelişiyor ve hayatımızı
 değiştiriyor. Günümüzde yapay zeka uygulamaları pek çok 
 farklı alanda kullanılıyor. Teknoloji geliştikçe zeka 
 kavramı ve teknoloji tanımı da yeniden şekilleniyor. 
 Bu değişim hayatımızı ve geleceğimizi 
 doğrudan etkiliyor. Hızla ilerleyen teknoloji, g
 eleceğimizin temelini oluşturuyor.


Kelime,Frekans
{'alanda': 1,
 'bu': 1,
 'da': 1,
 'değişim': 1,
 'değiştiriyor': 1,
 'doğrudan': 1,
 'etkiliyor': 1,
 'farklı': 1,
 'geleceğimizi': 1,
 'geleceğimizin': 1,
 'gelişiyor': 1,
 'geliştikçe': 1,
 'günümüzde': 1,
 'hayatımızı': 2,
 'hızla': 2,
 'ilerleyen': 1,
 'kavramı': 1,
 'kullanılıyor': 1,
 'oluşturuyor': 1,
 'pek': 1,
 'tanımı': 1,
 'teknoloji': 3,
 'teknolojileri': 1,
 'temelini': 1,
 'uygulamaları': 1,
 've': 3,
 'yapay': 2,
 'yeniden': 1,
 'zeka': 3,
 'çok': 1,
 'şekilleniyor': 1}
"""
import re
import pprint


def main():
    metin = dosya_oku('metin.txt')
    if metin is not None:
        sonuc = kelime_frekansi(metin)
        pprint.pprint(sonuc)
    



def kelime_frekansi(metin):
    temiz_metin = metin.replace("İ", "i").replace("I", "ı").lower()
    kelime_listesi = re.findall(r"\b\w+\b", temiz_metin)
    sayili_kelime_listesi = {}
    for kelime in kelime_listesi:
        sayili_kelime_listesi.setdefault(kelime,0)
        sayili_kelime_listesi[kelime] = sayili_kelime_listesi[kelime] + 1
    sirali_liste = dict(sorted(sayili_kelime_listesi.items()))
    return sirali_liste   

def dosya_oku(dosya_yolu):
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            metin = dosya.raed()
            return metin
    except FileNotFoundError:
        print(f"Hata: '{dosya_yolu}' adında bir dosya bulunamadı.")
        return None
    """except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None"""




main()