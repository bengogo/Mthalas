class Solution:
    def memLeak(self, memory1: int, memory2: int):
        i = 0
        while(True):
            if memory1-i<0 and memory2-i<0:
                return [i,memory1,memory2]
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i+=1
s=Solution()
print(s.memLeak(2,2))
print(s.memLeak(8,11))
print(s.memLeak(0,0))
print(s.memLeak(2**31-1,2**31-1))