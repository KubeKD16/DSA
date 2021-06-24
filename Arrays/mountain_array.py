"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

def check_if_mountain_array(arr):
    peak = 0
    left = 0
    right = 0

    while peak < len(arr)-1 and arr[peak] < arr[peak+1]:
        peak += 1
        left += 1

    while peak < len(arr)-1 and arr[peak] > arr[peak+1]:
        peak += 1
        right += 1

    return left * right > 0 and peak == len(arr)-1



s = [0,3,2,1]
s2 = [3,5,5]
print(check_if_mountain_array(s))
print(check_if_mountain_array(s2))