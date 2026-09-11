def main():

    while True:
        my_input = input("Is anagram?: ")
        is_panagram(my_input)

def is_panagram(my_sentence):
    EACH_LETTER = []
    for i in my_sentence:
        if i.upper() not in EACH_LETTER and i.isalpha():
            EACH_LETTER.append(i.upper())
        
    if len(EACH_LETTER) == 26:
        print('The sentence is a panagram')
    else:
        print('not panagram')
        print(len(EACH_LETTER))


main()