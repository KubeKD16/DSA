class Solution:
    def minRemoveToMakeValid(self,s):
        s = list(s)
        stack = []
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        while stack:
            s[stack.pop()] = ''

        return ''.join(s)







x = Solution()
string = "lee(t(c)o)de)"
s2 = "(a(b(c)d)"
# xf = x.minRemoveToMakeValid(string)
# print(xf)

y = Solution()
xf1 = y.minRemoveToMakeValid(s2)
print(xf1)
