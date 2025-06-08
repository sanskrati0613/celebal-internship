if __name__ == '__main__':

    n = int(input("Enter number of elements in tuple:"))
    print(f"Enter {n} space seperated integer:")
    Tuple1 = map(int, input().split())
    t = tuple(Tuple1)

    print(hash(t))

