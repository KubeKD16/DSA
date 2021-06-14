## check if all chars in string are unique


def isUnique(S):
    isunique = True
    for s in S:
        if len(s) == 0:
            print("String can't be empty")
            return 0
        for char in s:
            if s.count(char) > 1:
                isunique = False
                printFunction(isunique, s)
                break

        if(isunique):
            printFunction(isunique, s)




def printFunction(isunique,s):
    if (isunique):
        print("{} is unique".format(s))
        return True
    else:
        print("{} is not unique".format(s))
        return False

s = ["abc","kedar","aabbccddee","pooja","testing"]
isUnique(s)