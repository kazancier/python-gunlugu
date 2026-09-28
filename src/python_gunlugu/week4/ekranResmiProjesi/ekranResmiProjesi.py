from pathlib import Path
import subprocess
import time
from send2trash import send2trash


def main():
    masaustu = Path.home() / "Desktop" 
    hedef_yol = Path.home() / "Desktop" / "Çeşitli Dökümanlar"

    ekran_goruntuleri = ekran_resimlerini_getir(masaustu)

    if not ekran_goruntuleri:
        print("Ekran görüntüsü bulunamadı.")
        return

    print(f"Masaüstünde {len(ekran_goruntuleri)} tane ekran görüntüsü bulundu.\n")

    for ekran_goruntusu in ekran_goruntuleri:
        # Karar alma ve aksiyonu uygulama mantığı main akışına çekildi
        gerekli_mi = ekran_goruntusu_gerekli_mi(ekran_goruntusu)

        if gerekli_mi:
            yeni_isim(ekran_goruntusu, hedef_yol)
        else:
            tasi_cop(ekran_goruntusu)


def ekran_resimlerini_getir(target_path):
    ekran_goruntuleri = []

    if not target_path.exists():
        print(f"Klasör bulunamadı: {target_path}")
        return ekran_goruntuleri

    gecerli_uzantilar = {".jpg", ".jpeg", ".png"}

    for dosya in target_path.iterdir():
        isim = dosya.name
        isim_uygun = isim.startswith("Ekran Resmi") or isim.startswith("Screenshot")
        uzanti_uygun = dosya.suffix.lower() in gecerli_uzantilar

        if isim_uygun and uzanti_uygun:
            ekran_goruntuleri.append(dosya)

    return ekran_goruntuleri


def ekran_goruntusu_gerekli_mi(ekran_goruntusu):
    """DÜZELTME 2: Bu fonksiyon artık tek bir iş yapıyor:

    Dosyayı gösterir, kullanıcıya sorar ve sadece True/False kararı döner.
    """
    subprocess.run(["open", str(ekran_goruntusu)])
    time.sleep(3)
    subprocess.run(["osascript", "-e", 'quit app "Preview"'])

    while True:
        cevap = (
            input(
                f"Bu ekran görüntüsü gerekli mi ? \n {ekran_goruntusu.name} \n (E/H): "
            )
            .strip()
            .upper()
        )

        if cevap == "E":
            return True
        elif cevap == "H":
            return False

        print("Anlayamadım, lütfen sadece 'E' veya 'H' girin.")


def tasi_cop(ekran_goruntusu):
    if ekran_goruntusu.exists():
        send2trash(ekran_goruntusu)
        print(f"'{ekran_goruntusu.name}' çöp kutusuna taşındı.\n")
    else:
        print("Dosya bulunamadı.\n")


def yeni_isim(ekran_goruntusu, hedef_yol):
    hedef_klasor = hedef_yol
    hedef_klasor.mkdir(parents=True, exist_ok=True)

    while True:
        girilen_isim = input(
            "Dosya için yeni bir isim girin (uzantısız): "
        ).strip()

        if not girilen_isim:
            print(
                "Hata: Dosya ismi boş olamaz! Lütfen geçerli bir isim girin."
            )
            continue

        yeni_dosya_yolu = (
            hedef_klasor / f"{girilen_isim}{ekran_goruntusu.suffix}"
        )

        if yeni_dosya_yolu.exists():
            print(
                f"Hata: '{yeni_dosya_yolu.name}' adında bir dosya zaten var! Başka bir isim girin."
            )
            continue

        break

    ekran_goruntusu.rename(yeni_dosya_yolu)
    print(
        f"Başarılı! '{ekran_goruntusu.name}' -> '{yeni_dosya_yolu.name}' olarak taşındı.\n"
    )


if __name__ == "__main__":
    main()