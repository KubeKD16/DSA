def reverse(integer):
    """ get the LSB of the integer & add it to result * 10 & then divide the remaining integers from reverse by 10"""
    result , integer_remaining = 0 , abs(integer)

    while integer_remaining:
        result = result * 10 + integer_remaining % 10
        integer_remaining = integer_remaining // 10

    return -result if integer < 0 else result






print(reverse(11032))
print(reverse(1132))