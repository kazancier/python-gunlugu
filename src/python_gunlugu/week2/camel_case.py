#kullanıcıdan metni almak

#metni harflere ayırıp listeye yazmak

#liste üzerinde gezinip büyük harf aramak
    # büyük harf yoksa direk metni çıktıya yaz
    #nüyük harf varsa büyük harf öncesi + _ + büyük harf ve sonrasını yazdır.


def main():
    camel_case = input("give me camel case to convert snake case: ")

    letters = list(camel_case)
    snake_case = ""
    for letter in letters :
        if letter.islower():
           snake_case += letter
        else:
            snake_case = snake_case + "_" + letter.lower() 

    print(snake_case)



main()           


