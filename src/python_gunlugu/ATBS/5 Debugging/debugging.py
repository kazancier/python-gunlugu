def main():
    while True:
        my_name = get_name()
        assert my_name != "...", "You did not enter a name."
        if my_name == 'Ertugrul':
            print('Reis Hoşgeldin!')
        else:
            print(f'Hello {my_name}!')

def get_name():
    print('Enter your name:')
    name = input()
    if name == '':
        raise Exception('You did not enter a name.')

    return name



main()