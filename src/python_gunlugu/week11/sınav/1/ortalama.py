def main():
    girdi_list, gecersiz_list = sayi_al()
     

    ortalama = ortalama_cikti(girdi_list)
    ortalama_ikili = round(ortalama,2)
    print(f"Geçersiz, atlandı: {gecersiz_list} /n Adet: {len(girdi_list)}, Ortalama: {ortalama_ikili}")

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