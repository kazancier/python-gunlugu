# Ekran Resmi Düzenleyici

Masaüstündeki ekran görüntülerini otomatik tespit eden, kullanıcıya önizleme ile gösterip onay alan, seçime göre dosyaları yeniden adlandırıp hedef klasöre taşıyan veya çöp kutusuna atan Python aracı.

---

## Özellikler

- **Görsel Önizleme:** Görselleri macOS `Preview` uygulaması ile 3 saniye açıp kapatır.
- **Güvenli Taşıma:** Hedef klasörde aynı isimde dosya varsa üzerine yazmaz, kullanıcıyı uyararak yeni isim ister.
- **Çöp Kutusu Desteği:** Silinen dosyaları kalıcı olarak silmez, `send2trash` ile güvenli şekilde çöp kutusuna gönderir.
- **Loglama (Günlük):** Yapılan tüm işlemleri zaman damgasıyla birlikte `gunluk.json` dosyasına kaydeder.
- **Simülasyon Modu (`--dry-run`):** Dosya sisteminde değişiklik yapmadan prova çalıştırması sağlar.

---

## Kurulum

Projeyi çalıştırmak için gerekli bağımlılıkları yükleyin:

```bash
uv pip install send2trash

Çalıştırmak için 

python src/python_gunlugu/week4/ekranResmiProjesi/ekranResmiProjesi.py

Proje argparse ile 3 farklı parametre destekler:

--klasor	-	Kaynak masaüstü klasörü	
default :test
--hedef	-	İşlenen dosyaların taşınacağı klasör	
default :test_hedef
--dry-run	-	Değişiklik yapmadan simülasyon çalıştırır	


Mevcut Sınırlamalar ve Çalışma Mantığı
Aynı İsimli Dosya Çakışması: Hedef klasörde (hedef_yol) girilen yeni isimde bir dosya zaten mevcutsa, sistem mevcut dosyanın üzerine yazmaz. Hata mesajı basarak kullanıcıdan yeni bir isim girmesini ister.

İşlem Günlüğü: Gerçekleşen işlemler (E veya H kararları) betiğin bulunduğu dizindeki gunluk.json dosyasına işlenir. Silme (H) durumunda yeni_ad alanı null olarak kaydedilir.

Platform Bağımlılığı: Önizleme (open ve osascript) komutları macOS işletim sistemine özeldir.