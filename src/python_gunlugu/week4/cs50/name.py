import sys

"""
if len(sys.argv) > 2:
    print("Two many arguments")
elif len(sys.argv) < 2:
    print("Two few arguments")
else:
    print("Hi my name is:" , sys.argv[1])

"""


if len(sys.argv) > 2:
    sys.exit("Two many arguments")
elif len(sys.argv) < 2:
    sys.exit("Two few arguments")

print("Hi my name is:" , sys.argv[1])
