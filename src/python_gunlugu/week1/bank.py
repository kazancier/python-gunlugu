def main():
    message = input("Greeting: ")
    if message.lower().startswith("hello"):
        print("$0")
    elif message.lower().startswith("h"):
        print("$20")
    else:
        print("$100")

main()