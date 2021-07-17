class Solution:
    def wordBreak(self,s,wordDict):
        n = len(s)
        # print(n)
        dp = [False for i in range(n+1)]
        # print(dp)
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True

        return dp[-1]






x = Solution()
s1 = "leetcode"
word = ["leet","code"]
xf = x.wordBreak(s1,word)
print(xf)