import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    s_list = list(s)
    noktalama_ve_bosluk = set(string.punctuation + " ")

    #2 karakter ile 6 karakter arasında değilse return false
    if len(s_list)<2 or len(s_list)>6 :
        return False

    # period, space yada punctuation mark varsa return false 
    elif any(s in noktalama_ve_bosluk for s in s_list):
        return False

    #ilk iki harf letter değilse return false
    elif any(s.isdigit() for s in s_list[:2]):
        return False

    #plakada sayı varsa sayıdan sonra harf gelirse return false
    elif any(s.isdigit() for s in s_list):
        sayi_goruldu_mu = False
        sifir_goruldu_mu = False
        for s in s_list:
            
            if s.isdigit():
                if s == "0" and not sayi_goruldu_mu:
                    return False
                sayi_goruldu_mu = True
                if s == "0":
                    sifir_goruldu_mu = True
                
                           
            elif s.isalpha() and sayi_goruldu_mu:
                return False   
                    
        return True   
    # plakada birden fazla sayı varsa ilk sayı 0 olursa return false
    
    else:
        return True


main()