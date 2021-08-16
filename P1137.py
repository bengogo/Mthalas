# tribonacci Tn=Tn-1+Tn-2+Tn-3
class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        if n > 2:
            for _ in range(n-2):
                ans = [ans[1],ans[2],ans[0]+ans[1]+ans[2]]
            return ans[-1]
        return ans[n]
s=Solution()
for n in range(10):
    print(s.tribonacci(n))