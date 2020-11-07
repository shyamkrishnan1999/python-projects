def printhash(size):
    for i in range(0, size):
        print("-", end="")


def print_rangoli(size):
    # Top portion
    ch = chr(ord('a') + size - 1)
    lsize = 2 * size - 2
    k = lsize
    mid = 1
    for i in range(0, size - 1):
        printhash(lsize)
        kstr = ch
        for j in range(0, mid):
            print(kstr, end="")
            print("-", end="")
            if j < mid / 2 - 1:
                kstr = chr(ord(kstr) - 1)
            else:
                kstr = chr(ord(kstr) + 1)

        printhash(lsize - 1)
        lsize -= 2
        mid += 2
        print("")

    # middle portion
    kstr = ch
    count = 0
    for j in range(0, mid):
        print(kstr, end="")
        if j == mid - 1:
            break
        else:
            print("-", end="")
            if j <= mid / 2 - 1:
                kstr = chr(ord(kstr) - 1)
            else:
                kstr = chr(ord(kstr) + 1)

    lsize += 2
    print("")

    # Bottom portion
    for i in range(0, size - 1):
        printhash(lsize)
        kstr = ch
        count = 0
        for j in range(0, mid - 2):
            print(kstr, end="")
            print("-", end="")
            if j <= mid / 2 - 2:
                kstr = chr(ord(kstr) - 1)
            else:
                kstr = chr(ord(kstr) + 1)

        printhash(lsize - 1)
        lsize += 2
        mid -= 2
        print("")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)