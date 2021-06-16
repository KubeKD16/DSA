"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Developed by Kedar Pandhare
"""
def sortedSquares(nums):
    sorted_array = []

    for i in nums:
        sorted_array.append(i ** 2)

    return sorted(sorted_array)

nums = [-7,-3,2,3,11]
test = sortedSquares(nums)
print(test)