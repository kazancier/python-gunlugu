def main():
    #  Amount Due 50 cent yaz ve para sor

    # parayı 50 ile kıyasla fazlaysa  Change Owed yaz

    # para eksikse 50 'den çıkartıp Inser Coin yaz
    loops = True
    amount_due = 50
    while loops:
        insert_coin = int(input(f"Amount Due: {amount_due} \nInsert Coin: "))
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            amount_due = amount_due - insert_coin
            if amount_due <= 0:
                print(f"Change Owed: {abs(amount_due)}")
                loops = False

            

main()

  