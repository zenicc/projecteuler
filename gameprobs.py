def do_something():
    first = 5/3
    second = 7/3
    third = 9/3
    fourth = 11/3

    for n in range(4):
        print(first**n)
        print(second**n)
        print(third**n)
        print(fourth**n)
        print()


if __name__ == '__main__':
    do_something()