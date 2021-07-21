"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

 

Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

"""
from collections import deque
class Solution:
    def __init__(self):
        pass 

    def reverse(self,s):
        # print("inside loop")
        l , r = 0, len(s) - 1
        while l < r:
            """ Removes the trailing and starting blank spaces in string """
            while s[l] == ' ' and l < r:
                l += 1
            while s[r] == ' ' and l < r :
                r -= 1
            
            d,w = deque(), []

            while l <= r:
                if s[l] == ' ' and w:
                    """ if I see a blank in-between 2 words & words is not empty, append the contents of word as a string in Deque """
                    d.appendleft(''.join(w))
                    w = []
                elif s[l] != ' ':
                    """ If i don't see any blank spaces after removing the trailing edges, keep appending the chars to the word list"""
                    w.append(s[l])
                l += 1
            
            d.appendleft(''.join(w))
            
        return ' '.join(d)
            





class main:
    if __name__ == '__main__':
        x = Solution()
        strings = ["the sky is blue",
                   "  Bob    Loves  Alice   ", "a good   example"]
        print(strings)
        for i in strings:
            xf = x.reverse(i)
            print(xf)
