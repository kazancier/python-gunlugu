def main():
    message =str(input())
    if message.endswith(":("):
        print(message.replace(":(","🙁"))
    elif message.endswith(":)"):
        print(message.replace(":)","🙂"))
    else:
        print(message)
main()