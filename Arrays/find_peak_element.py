def fin_peak(nums):
    l, r = 0, len(nums) - 1
    while l < r - 1:
        mid = int((l + r) / 2)
        """ if mid is greater than it's right and left element then return mid"""
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid

        if nums[mid] < nums[mid + 1]:
            """ if middle is less than it;s right element, then consider the right sub-list and make left as the first element of that list"""
            l = mid + 1
        else:
            """ else, push right to the left sub-list on the left of the mid element"""
            r = mid - 1

    """ below condition handles when there are only 2 elements in the list"""
    return l if nums[l] >= nums[r] else r


print(fin_peak([1,2,1,3,5,6,4]))
print(fin_peak([1,2,3,1]))
