def main():
    name = input("Name?: ")
    if name =="":
        name = two_fer()
    else:
        name = two_fer(name)
    print(name)

def two_fer(name="you"):
        return f"One for {name}, one for me."

main()