def find_disappeared(n):
    for i in range(len(n)):
        temp = abs(n[i])-1
        if n[temp] > 0:
            n[temp] *= -1

    res = []
    for i,j in enumerate(n):
        if j > 0:
            res.append(i+1)

    return res








print(find_disappeared([4,3,2,7,8,2,3,1]))