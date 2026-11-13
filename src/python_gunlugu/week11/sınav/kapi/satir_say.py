import sys
from pathlib import Path

def main():

    if len(sys.argv) < 2:
        print(f"Kullanım: python satir_say.py <dosya>")
        sys.exit(1)

    dosya_yolu = sys.argv[1]
    yol = Path(dosya_yolu)    

    if yol.is_file():
        with open(yol, "r", encoding="utf-8") as dosya:
            icerik=dosya.read()
        
        satir_sayisi = len(icerik.splitlines())

        print(f"Satır sayısı : {satir_sayisi}")
    else:
        print(f"Dosya bulunamadı: {yol}")

if __name__ == "__main__":
    main()