"""
check if 2 strings are permutations of each other
Developed by Kedar Pandhare
"""

def isPermutation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s2 = " ".join(sorted(s2))
    s1 = " ".join(sorted(s1))
    """ this will sort the chars in the string and append it to a new string"""
    for i in range(0,len(s1),1):
        if s1[i] != s2[i]:
            return False

    return True

"""
Alternate approach of using Dictionary to store the keys and then compare with other string
"""

def test(s1,s2):
    character = {}
    count = 1

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i not in character:
            character[i] = count
        else:
            character[i] = count + 1

    for j in s2:
        if j not in character:
            return False
        else:
            character[j] -= 1

    if all(x ==0 for x in character.values()):
        return True
    else:
        return False


check_permutation = isPermutation("dcbba","abbcd")
check_permutation_1 = test("dcbba","abbcd")

"""
This method uses HASH Map where you store the element of a string in Hash map and then check the occurence
of elements in 2nd string in hashmap and return true if all the values of the string elements is 0
"""

if(check_permutation_1):
    print("Two strings are permutations of each other")
else:
    print("Two strings are not permutations of each other")

"""
This method sorts the strings s1 and s2 and checks each element of both s1 and s2
and returns true if all of them match
"""

if(check_permutation):
    print("Two strings are permutations of each other")
else:
    print("Two strings are not permutations of each other")