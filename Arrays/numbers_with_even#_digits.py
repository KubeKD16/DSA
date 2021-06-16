"""
Given an array nums of integers, return how many of them contain an even number of digits.

Developed by Kedar Pandhare
"""
def findNumbers(nums):
    count = 0
    for i in nums:
        if (len(str(i)) % 2 == 0):
            count += 1

    return count

test = findNumbers([555,901,482,1771,12345678])
print(test)