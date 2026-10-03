Bu araç masaüstüne yer alan önemsiz ekran resimlerini çöp sepetine gönderir. Önemli ekran resimlerinin ismini değiştirerek çeşitli dökümanlar klasörüne taşır. Araç resimlerin önemli/önemsiz olduğuna karar vermez. Kararı kullanıcı verir.  + Kontrol

Araç resmin önemli / önemsiz olduğunu sorar. Önemli ise yeni ismini sorar ve resmi çeşitli dökümanlara taşır. +  Kontrol

Verilen Cevap "E" ise Ekran Resminin yeni ismini sorar
Cevap "H" ise çöp kutusuna taşır
Cevap bu ikisi dışında birşey ise 
"Anlayamadım, lütfen sadece 'E' veya 'H' girin." + Kontrol 

Önemsiz ise çöp sepetine taşır. Yanlış bir sınıflandırmayı geri alabilmek için silmez çöp kutusuna taşır. + Kontrol

st_atime resim görüntülenmede güncellenmiyor. Bunu denedim ve sonrasında araştırdım işletim sistemi performans gerekçesiyle güncellemiyor.O yüzden onu kullanmaz. + Kontrol

Masaüstünde hiç ekran görüntüsü yoksa bunun bilgisini verir. + Kontrol

Önemli ekran görüntüsü için verdiğin isimde başka dosya varsa seni uyarır ("Hata: '{yeni_dosya_yolu.name}' adında bir dosya zaten var! Başka bir isim girin."
"+ Kontrol
Boş isimle Enter'a basarsan kabul etmez dosya ismi boş olamaz der ve tekrar sorar.  + Kontrol (Hata: Dosya ismi boş olamaz! Lütfen geçerli bir isim girin.")ve yeni isim ister. )

Bilinen Sınırlar :

Eğer yeni dosya isminde "/" var ise hata döner

Hedef ve Kaynak klasörler kullanıcıya çalıştırırken tanımlar.

Kullanıcı kaynak klasörü vermez ise Default olarak Desktop\test kullanılır. Yazılımın amacaı masaüstündeki Ekran resimlerini temizlemek.

Kullanıcı hedef klasörü vermez ise Masaüstünde Çeşitli Dökümanlar isminde bir klasör oluşturulur ve dökümanlar buraya kayıt edilir.

Örnek :

python ekranResmiProjesi.py ~/Desktop ~/Desktop/Çeşitli\ Dökümanlar

Desktop klasöründe 4 Ekran Resmi bulundu.

python ekranResmiProjesi.py ~/Desktop ~/Desktop/Çeşitli\ Dökümanlar --dry-run

Desktop/Test klasöründe 4 Ekran Resmi bulunacaktı.

python ekranResmiProjesi.py

Desktop klasöründe 4 Ekran Resmi bulundu.

python ekranResmiProjesi.py 'Subtop' 

Hata : Kaynak klasör bulunamadı çıkış kodu 1


JSON Gunluk :

Dosya hareketlerinin tarihçesi json dosyasında tutulur. Provalar gürültü oluşturmamak için kayıt edilmez.

Hedef ve kaynak klasörler değişebileceği için Gunluk dosyası proje klasöründe yer alacaktır. 





