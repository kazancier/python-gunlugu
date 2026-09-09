# prompt user for item
# one per line until contrl + D
# return $ total price , case insentisitively



menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        try:
            item = input("Item: ").strip().title() 
            total += float(menu.get(item, 0))
            print(f"Total: ${total:.2f}")
        except EOFError:
            break

        
        

main()