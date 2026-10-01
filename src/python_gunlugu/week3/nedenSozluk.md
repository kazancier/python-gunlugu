listelerde indexler 0 'dan başlar ve sıralı devam eder.
sözlüklerde ise key value ikisi de yönetilebilir.
kelime frekans projesinde olduğu gibi ;
örnek 100.000 kelimelik bir metin 8000 kelime sayılacağı zaman liste kullanırsak her bir kelime için metni tekrar okumak gerekir. Bu toplamda 800.000.000 işleme sebep olur.
Ama sözlük ile 100.000 kelimelik metni bir kez okumak yeterli olacaktır. Toplamda 100.000 işlem yapılacaktır. Kelime başına bir işlem.

Sözlükte arka planda bir hash tablosu yapısı vardır. Bir kelime eklendiğinde o hash tablosuna eklenir. Tüm elemanları taramadan doğrudan o kelimeye key olarak erişilebilir.

Hash Fonksiyonu kelimeden doğrudan bir sayı hesaplayarak bellekteki adresini belirler. Dolayısıyla arama yapılmaz hesaplama ile yeri bulunur