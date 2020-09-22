if __name__ == '__main__':
    s = input()
    alnum=alpha=digi=lower=upper=False
    for ch in s:
        if ch.isalnum():
            alnum=True
        if ch.isalpha():
            alpha=True
        if ch.isdigit():
            digi=True
        if ch.islower():
            lower=True
        if ch.isupper():
            upper=True

    print(alnum)
    print(alpha)
    print(digi)
    print(lower)
    print(upper)
