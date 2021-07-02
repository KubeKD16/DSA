def zerotoRight(nums):
    if nums == None and len(nums) == 0: return False
    i = 0
    j = 1
    length = len(nums)
    zeros = 0

    while i < len(nums):
        if nums[i] == 0:
            zeros += 1
            # if j < len(nums) and nums[j] == 0:
            #     nums.pop(j)
            #     j = j+1

            nums.pop(i)
            # nums.append(0)
            length -= 1
            i -= 1

        # else: i += 1

        i += 1

    for j in range(zeros):
        nums.append(0)

    return nums

s = [0,1,0,3,12,99,8,0,0,5]
s1=[0,0,1]
# print(zerotoRight(s))
print(zerotoRight(s))