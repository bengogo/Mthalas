# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]= (dp[i-2] if i>=2 else 0) + 2
                elif (i-dp[i-1]) > 0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+(dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0)+2
        return max(dp)

import random
s=Solution()
l = ['(' if random.randint(0,1)==0 else ')' for _ in range(10)]
l=''.join(l)
print(l)
print(s.longestValidParentheses(l))

                    