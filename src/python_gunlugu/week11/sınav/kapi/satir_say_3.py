import argparse
import sys
from pathlib import Path

def main():

    prs = argparse.ArgumentParser()
    prs.add_argument("dosya")
    arg = prs.parse_args()

   
    dosya_yolu = arg.dosya

    if dosya_yolu == "":

        print("Kullanım : python satir_say_3.py <dosya adı>")
        exit(1)

    else:


        yol = Path(dosya_yolu)

        if yol.is_file():
            with open(yol , mode ="r",encoding="UTF-8") as dosya:
                content = dosya.read()

            satir = len(content.splitlines())

            print(f"Satir Sayısı : {satir}")

        else:
            print("Dosya bulunamadı")
            sys.exit(1)    







if __name__ == "__main__":
    main()