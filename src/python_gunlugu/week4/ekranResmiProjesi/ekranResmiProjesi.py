from pathlib import Path


masaustu = Path.home() / "Desktop"
hedef_klasor = Path.home() / "Desktop" / "Çeşitli Dökümanlar"

ekran_goruntuleri = []

for dosya in masaustu.iterdir():
    if dosya.is_file() and (dosya.name.startswith("Ekran Resmi") or dosya.name.startswith("Screenshot")) and (dosya.name.endswith("jpg") or dosya.name.endswith("jpeg") or dosya.name.endswith("png")):
        ekran_goruntuleri.append(dosya)


if len(ekran_goruntuleri) == 0:
    print("Ekran görüntüsü bulunamdı")
else:
    print(f"Masaüstünde {len(ekran_goruntuleri)} tane ekran görüntüsü bulundu.\n")
    print(ekran_goruntuleri)

 
