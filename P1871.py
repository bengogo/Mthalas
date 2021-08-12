'''
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

    i + minJump <= j <= min(i + maxJump, s.length - 1), and
    s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1': return False
        n = len(s)
        cs = list(s)
        cs[0] = '2'
        maxnext = 0
        for i in range(0,n):
            if cs[i] == '2':
                maxnext = max(maxnext,i+minJump)
                while maxnext <= min(n-1,i+maxJump):
                    if cs[maxnext]=='0': cs[maxnext]='2'
                    maxnext+=1
                if cs[-1] == '2': return True
        return False
                 

    def canReachUseDP(self, s: str, minJump: int, maxJump: int) -> bool:  
        n = len(s)
        fn = [0]*n
        pre = [0]*n
        fn[0] = 1
        for i in range(minJump):
            pre[i]=1
        
        for i in range(minJump,n):
            l = i-maxJump
            r = i-minJump
            if s[i] == '0':
                val = pre[r]-(0 if l <=0 else pre[l-1])
                fn[i] = int(val!=0)
            pre[i] = pre[i-1] + fn[i]
        return fn


import random
s=Solution()
a=[str(random.randint(0,1)) for i in range(10)]
a[0]='0'
a[-1]='0'
a=''.join(a)
b = [int(i) for i in a]
print(b)
print(s.canReach(a,2,3))