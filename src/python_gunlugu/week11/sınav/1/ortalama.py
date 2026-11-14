def main():
    girdi_list, gecersiz_list = sayi_al()
    gecersiz_list_cikti = ""
    for i in gecersiz_list:
        gecersiz_list_cikti += f"Geçersiz, atlandı: {i}\n"
    if len(girdi_list) != 0:
        ortalama = ortalama_cikti(girdi_list)
        print(f"{gecersiz_list_cikti}Adet: {len(girdi_list)}, Ortalama: {ortalama:.2f}")
    else:
        print(f"{gecersiz_list_cikti}Sayı girilmedi.")
def sayi_al():
    durum= True
    girdi_list = []
    gecersiz_list =[]
    while durum:       
        girdi =input()
        try:
            girdi_float = float(girdi)
            girdi_list.append(girdi_float)
        except ValueError:
            if girdi == "":
                durum = False
                break
            gecersiz_list.append(girdi)
    return girdi_list,gecersiz_list



def ortalama_cikti(my_list):
    toplam = 0
    for i in my_list:
        toplam += i

    ortalama = toplam / len(my_list)
    return ortalama
        


if __name__ == "__main__":
    main()