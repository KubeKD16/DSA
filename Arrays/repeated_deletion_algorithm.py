def repeated(a):
    prev = 0
    next = 1

    if a is None and len(a) == 0: return False

    while next < len(a):
        if a[prev] == a[next]:
            next += 1
            # prev += 1
        elif a[prev] != a[next]:
            a[prev+1] = a[next]
            prev += 1
            # prev = next-1

    return a[:prev+1]




t1=[1, 1, 2]
t2=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(repeated(t1))

print(repeated(t2))