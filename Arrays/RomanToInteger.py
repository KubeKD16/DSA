def romanToInteger(num):
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev = None
    for letter in num[::-1]:
        value = map[letter]

        if ((letter == 'I' and prev in ('V','X'))) or ((letter == 'X' and prev in ('L','C'))) or ((letter == 'C' and prev in ('D','M'))):
            result = result - value
        else:
            result = result + value

        prev = letter

    return result

string1 = 'LVIII'
print(romanToInteger(string1))