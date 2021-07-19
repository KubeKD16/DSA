
def convert_to_word(nums):
    units = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
    'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    # print(units)
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    # print(tens)

    def to_word(nums):
        if nums < 20:
            return units[nums-1:nums]
        
        if nums < 100:
            return [tens[nums//10 - 2]] + to_word(nums % 10)
        
        if nums < 1000 :
            return [units[nums//100 - 1]] + ['Hundred'] + to_word(nums % 100)


        for i,j in enumerate(('Thousand','Million','Billion'),1):
            if nums < 1000 ** (i+1):
                return to_word(nums//(1000 ** i)) + [j] + to_word(nums % 1000 ** i)
    
    return ' '.join(to_word(nums))






numbers = [10,99,89,850,123, 999, 150897, 90087645]
for i in numbers:
    value = convert_to_word(i)
    print("The word value of {} is {}".format(i,value))


