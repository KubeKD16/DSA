def test(nums, k):
    d = {}
    d[0] = 1
    c = 0
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        c += d.get(sum - k, 0)
        d[sum] = d.get(sum, 0) + 1

    return c


n = [1, 1, 1]
val = 2
print(test(n, val))