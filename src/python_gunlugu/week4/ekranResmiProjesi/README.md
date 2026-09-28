# Screen Cleaner Tool

Masaüstündeki ekran görüntülerini sırayla Önizleme (Preview) uygulamasında açıp kullanıcının onayına sunan, seçime göre dosyaları yeniden adlandırarak arşivleyen veya çöp kutusuna taşıyan Python tabanlı bir otomasyon aracıdır.

---

## Ne Yapar

* **Ekran Görüntülerini Tutar:** Belirtilen klasördeki (`Desktop`) yalnızca `"Ekran Resmi"` veya `"Screenshot"` ile başlayan ve `.jpg`, `.jpeg`, `.png` uzantılı dosyaları tespit eder.
* **Görsel Önizleme Sağlar:** Her bir görseli macOS Önizleme (Preview) uygulamasında 3 saniye boyunca otomatik açıp incelenmesine olanak tanır ve ardından kapatır.
* **Dosya Yönetimi ve Arşivleme:**
  * **Sakla (E):** Kullanıcıdan yeni bir dosya adı alarak dosyayı uzantısını koruyacak şekilde Hedef Klasöre (`Desktop/Çeşitli Dökümanlar`) taşır.
  * **Sil (H):** Dosyayı kalıcı olarak silmek yerine macOS Çöp Kutusu'na güvenli bir şekilde aktarır (`send2trash`).
* **Çakışma ve Boş İsim Kontrolü:** İsim çakışmalarını ve boş dosya adı girişlerini engelleyen doğrulama mekanizmalarına sahiptir.

---

## Nasıl Kurulur

Script bağımlılık olarak yalnızca `send2trash` kütüphanesini gerektirir.

1. **Gereksinimleri Yükleyin:**
   ```bash
   pip install send2trash

Nasıl Çalıştırılır

Kod dosyanızın bulunduğu dizine terminal üzerinden erişin:

cd /dosyanizin/bulundugu/dizin

Terminal üzerinden Python betiğini başlatmanız yeterlidir:

python main.py

Betik çalıştığında, karşılaştığı her ekran görüntüsü için terminalde (E/H) seçeneği sunacaktır:

E girilirse: Terminal sizden uzantısız yeni bir isim ister ve dosyayı Çeşitli Dökümanlar klasörüne taşır.

H girilirse: Dosya send2trash ile güvenli şekilde çöpe atılır.

Bilinen Sınırlar
macOS Bağımlılığı: subprocess.run(["open", ...]) ve osascript (AppleScript) komutları kullanıldığı için kod yalnızca macOS sistemlerde çalışır. Linux veya Windows platformlarında çalışmaz.

Sabit Zamanlayıcı (3 Saniye): Önizleme penceresi her görsel için sabit olarak 3 saniye açık kalır; büyük veya detaylı inceleme gerektiren görseller için bu süre yetersiz kalabilir.

Önizleme Kapanma Çakışması: Kod quit app "Preview" komutunu çalıştırdığından, arka planda Önizleme uygulamasında açık olan diğer tüm pencereler/dokümanlar da kapatılır.

Sabit Dosya Yolları: Kaynak ve hedef dizinler (Desktop/Test ve Desktop/Çeşitli Dökümanlar) doğrudan kod içerisinde tanımlanmıştır (hardcoded); terminal parametresi veya yapılandırma dosyası desteği sunmaz.