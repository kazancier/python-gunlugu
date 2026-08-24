def main():
    qa = input("What is the Great Question of Life?")
    if qa_true(qa):
        print("Yes")
    else:
        print("No")

def qa_true(nn):
    if nn == "42":
        return True
    elif nn.lower() == "forty-two":
        return True
    elif nn.lower() == "forty two":
        return True
    else:
        return False


main()