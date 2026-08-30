def main():
    for i in [1,3,6,10,15,10,6,3,1]:
        print_square(i)

def print_square(size):
    for i in range(size):
        print("*" * size)

main()
