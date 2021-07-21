class Test:
    def longest_consecutive_sequence(self,s):
        best = 0

        for x in s:
            if x-1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                
                best = max(best,y-x)
        
        return best




class main:
    if __name__ == '__main__':
        strings = [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [100, 4, 200, 1, 3, 2],[4,2,9,0,0,54,55,56,57,58,59,9,31,23]]

        c1 = Test()
        for i in range(len(strings)):
            result = c1.longest_consecutive_sequence(strings[i])
            print("the longest consecutive sequence for {} is: {}".format(strings[i],result))


