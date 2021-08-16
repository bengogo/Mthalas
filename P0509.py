import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        return self.calc2(n)
    def calc1(self,n):
        a,b=0,1
        for _ in range(n):
            a,b = b,a+b
        return a
    def calc2(self,n):
        def matmul(a1,a2):
            ans=[[0,0],[0,0]]
            ans[0][0] = a1[0][0]*a2[0][0]+a1[0][1]*a2[1][0]
            ans[0][1] = a1[0][0]*a2[0][1]+a1[0][1]*a2[1][1]
            ans[1][0] = a1[1][0]*a2[0][0]+a1[1][1]*a2[1][0]
            ans[1][1] = a1[1][0]*a2[0][1]+a1[1][1]*a2[1][1]
            return ans
        def qpow(a,n):
            ans = [[1,0],[0,1]]
            while (n):
                #如果n的当前末位为1
                #ans乘上当前的a
                if(n&1):        
                    ans=matmul(a,ans)
                #a自乘
                a=matmul(a,a)
                #n往右移一位
                n >>= 1
            return ans
        f = [[0,1],[1,1]]
        f2 = qpow(f,n+1)
        return f2[0][0]
    def calc3(self,n):
        sqrt5 = 5**0.5
        fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
        return round(fibN / sqrt5)

s=Solution()
N = 10000
import time
st = time.time()
for i in range(N):
    s.calc1(i)
# print(s.calc1(N))
print(time.time()-st)
st = time.time()
for i in range(N):
    s.calc2(i)
# print(s.calc2(N))
print(time.time()-st)
# for i in range(N):
#     s.calc3(i)
# # print(s.calc2(N))
# print(time.time()-st)
