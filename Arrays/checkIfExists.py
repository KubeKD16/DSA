'''Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''

def checkifExists(arr):
    s = set()
    for j in arr:
        if 2 * j in s: return True

        if j % 2 == 0 and int(j/2) in s: return True
        s.add(j)

    return False

s = [7,1,14,11]
s1 = [10,2,5,3]
s2 = [3,1,7,11]


print(checkifExists(s))
print(checkifExists(s1))
print(checkifExists(s2))