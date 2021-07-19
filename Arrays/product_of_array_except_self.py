def product(arr):
    p = 1
    n = len(arr)
    map = {}
    output = []
    for i in range(len(arr)):
        output.append(p)
        p = p * arr[i]
    
    p = 1

    for j in range(n-1,-1,-1):
        output[j] = output[j] * p
        map[j] = output[j]
        p = p * arr[j]
    
    for k in range(n-1,-1,-1):
        arr[k] = map[k]
    
    return arr







print(product([1,2,3,4]))