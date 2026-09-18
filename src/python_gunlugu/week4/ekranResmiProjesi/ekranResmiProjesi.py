from pathlib import Path


masaustu = Path.home() / "Desktop"
hedef_klasor = Path.home() / "Desktop" / "Çeşitli Dökümanlar"

ekran_goruntuleri = []

for dosya in masaustu.iterdir():
    isim = dosya.name
    yol = dosya
   
    isim_uygun = isim.startswith("Ekran Resmi") or isim.startswith("Screenshot")
        
    
    uzanti_uygun = yol.suffix.lower() == '.jpg' or yol.suffix.lower() == ".jpeg" or yol.suffix.lower() == ".png"
        
    
    if isim_uygun and uzanti_uygun:
        ekran_goruntuleri.append(dosya)

if len(ekran_goruntuleri) == 0:
    print("Ekran görüntüsü bulunamdı")
else:
    print(f"Masaüstünde {len(ekran_goruntuleri)} tane ekran görüntüsü bulundu.\n")
    print(ekran_goruntuleri)

 
