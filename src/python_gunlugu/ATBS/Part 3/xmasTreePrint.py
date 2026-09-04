def main():

    tree_size = int(input("Tell me the size of tree: "))

    goes_on = True
   
    i = tree_size
    mi = 0
    while goes_on:
        satir = (" " * (i-1)) + "^" * (2*mi+1)   + " " * (i-1)
        print(satir)       
        i = i - 1
        mi = mi + 1
       

        if i == 0 :
            goes_on = False

        
    kareleri_yazdir(tree_size)


def kareleri_yazdir(num):
    print(" " * (num-1)+"#"+" " * (num-1))
    print(" " * (num-1)+"#"+" " * (num-1))

main()