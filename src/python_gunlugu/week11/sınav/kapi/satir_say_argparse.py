import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("dosya_yolu")

    args = parser.parse_args()        

    dosya_yolu = args.dosya_yolu
    
    yol = Path(dosya_yolu)    
    
    if yol.is_file():
        with open(yol, "r", encoding="utf-8") as dosya:
            icerik=dosya.read()
            
        satir_sayisi = len(icerik.splitlines())
    
        print(f"Satır sayısı : {satir_sayisi}")
    else:
        print(f"Dosya bulunamadı: {yol}")
        sys.exit(1)


if __name__ == "__main__":
    main()