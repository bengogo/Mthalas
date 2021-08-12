# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.calc1(s)
    # use dp,init dp = [0]*n ,modify dp value when s[i]==')'
    def calc1(self,s):
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]= (dp[i-2] if i>=2 else 0) + 2
                elif (i-dp[i-1]) > 0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+(dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0)+2
        return max(dp)

    # use stack
    def calc2(self,s):
        ans = 0
        stack = [-1]
        for i,v in enumerate(s):
            if v=='(':
                stack.append(i)
            else:
                stack.pop()
                if(len(stack)==0):
                    stack.append(i)
                else:
                    ans = max(ans,i-stack[-1])
        return ans
    # use double point
    def calc3(self,s):
        left,right = 0,0
        ans = 0
        for i in s:
            if i == '(': left+=1
            else: right +=1

            if left==right:
                ans = max(ans,2*right)
            elif right>left:
                left,right = 0,0
        left,right = 0,0
        for i in s[::-1]:
            if i == '(': left+=1
            else: right +=1

            if left==right:
                ans = max(ans,2*left)
            elif left>right:
                left,right = 0,0
        return ans

import random
s=Solution()
l = ['(' if random.randint(0,1)==0 else ')' for _ in range(100)]
l=''.join(l)
print(l)
print(s.longestValidParentheses(l))
print(s.calc2(l))
print(s.calc3(l))


                    