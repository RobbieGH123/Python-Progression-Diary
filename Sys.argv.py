import sys

while len(sys.argv) < 2:
    print("Too few")
    if len(sys.argv) > 3:
        print("too many")
print(f" Hello, my name is {sys.argv[1]}")

