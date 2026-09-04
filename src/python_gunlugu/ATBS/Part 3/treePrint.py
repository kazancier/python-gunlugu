tree_size = int(input("Tell me the size of tree: "))



for i in range(tree_size):
    print(" " * (tree_size-i-1), end= "")
    print("^" * (2*i-1), end= "")
    print(" " * (tree_size-i))

for i in range(2):
    print(" " * (tree_size-1), end= "")
    print("#", end= "")
    print(" " * (tree_size-1))