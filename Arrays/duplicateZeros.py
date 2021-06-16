"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Developed by Kedar Pandhare
"""
arr = [8,4,5,0,0,0,0,7]
for i in range(len(arr) - 1):
    if arr[i] == 0:
        if arr[i-1] == 0:
            i += 1
            # break
        else:
            arr = arr[:i] + [0] + arr[i:len(arr) - 1]
print(arr)