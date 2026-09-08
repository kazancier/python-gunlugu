def main():
    print_columns(3)
    print_rows(5)

def print_columns(height):
    """parametre kadar yükseklite bir # kolonu basar"""
    print("#\n" * height, end="")

def print_rows(width):
    """parametre kadar genişlikte bir ? satırı basar"""
    print("?" * width, end="")
main()

    