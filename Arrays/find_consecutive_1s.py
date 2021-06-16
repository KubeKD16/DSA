"""
Below code checks the max number of consecutive 1s in a given array

Developed by Kedar Pandhare
"""
def findMaxConsecutiveOnes(nums):
    result = []
    iterations = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            count += 1
            result.append(nums[i])
        elif nums[i] == 0:
            iterations.append(len(result))
            result = []
            count = 0

    if len(result) != 0:
        iterations.append(len(result))
    max_item = max(iterations)
    return max_item

test = findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
print(test)