
def convert_to_word(nums):
    units = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
    'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    # print(units)
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    # print(tens)

    def to_word(n):
        if n < 20:
            return units[n-1:n]
        
        if n < 100: 
            return [tens[n//10 - 2]] + to_word(n % 10)
        
        if n < 1000 :
            return [units[n//100 - 1]] + ['Hundred'] + to_word(n % 100)


        for i,j in enumerate(('Thousand','Million','Billion'),1):
            if n < 1000 ** (i+1):
                return to_word(n//(1000 ** i)) + [j] + to_word(n % 1000 ** i)
    
    return ' '.join(to_word(nums)) or 'Zero'






numbers = [10,99,89,850,123,999,150897,987645,98765334,1098762345]
for i in numbers:
    value = convert_to_word(i)
    print("The word value of {} is {}".format(i,value))


