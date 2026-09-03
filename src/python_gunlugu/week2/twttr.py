

def main():

    cumle = input("Input: ")
    cumle_list = list(cumle)
    cikti = ""
    for harf in cumle_list:
        if not unlu_harf_mi(harf):
            cikti += harf

    print(cikti)    


def unlu_harf_mi(harf):
    unluler = "aeıioöuüAEIİOÖUÜ"
    return harf in unluler

main()           


