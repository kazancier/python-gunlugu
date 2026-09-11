def main():

    my_coordinates = []
    while True:
        user_input = input("Coordinates? n/e/s/w (just in lowercase)")
        if user_input in ['n','s','e','w']:
            my_coordinates.append(user_input)
            print(f"Now coordinates are {my_coordinates}")
        elif user_input == "":
            break
        else:
            print('Unacceptable coordinates') 
            print(f"Now coordinates are {my_coordinates}")

    print(get_end_coordinates(my_coordinates))


def get_end_coordinates(coord_list):
    a = 0
    b = 0
    for i in coord_list:
        if i == 'n':
            b += 1
        elif i == 's':
            b -= 1
        elif i == 'e':
            a += 1
        elif i == 'w':
            a -= 1

    return [a,b]
    

main()