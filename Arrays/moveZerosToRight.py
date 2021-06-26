def zerotoRight(a):
    if a == None and len(a) == 0: return False
    i = 0
    length = len(a)

    while i < len(a):
        if a[i] == 0:
            a.pop(i)
            a.append(0)
            length -= 1
        else:
            i +=1

    return a

s = [0,1,0,3,12]
s1=[1,0,1]
# print(zerotoRight(s))
print(zerotoRight(s1))