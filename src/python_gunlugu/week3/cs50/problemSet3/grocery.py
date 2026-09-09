def main():
    gross = []

    while True:
        try:
            item = input("Item: ").strip().upper()
            gross.append(item)
        except EOFError:
            break

    gross.sort()
    print("\n\n")
    for item in set(gross):
        print(f"{gross.count(item)} {item}")

main()