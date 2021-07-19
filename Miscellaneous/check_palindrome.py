import math


def palindrome(integer):
    """ get the number of digits by using the formula NOD = |_(log10n)_| + 1



    """
    x = integer
    if x <= 0:
        return x == 0

    num_of_digits = math.floor(math.log10(integer)) + 1
    print(num_of_digits)
    msb_mask = 10 ** (num_of_digits - 1)
    # print(msb_mask)

    for i in range(num_of_digits // 2):
        if (x // msb_mask) != x % 10:
            return False
        x %= msb_mask
        # print(x)
        x //= 10
        msb_mask //= 100
        # print(msb_mask)

    return True







print(palindrome(1234554321))