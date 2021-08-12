class Solution:
    def maximumPopulation(self, logs) -> int:
        return self.calc1(logs)
    # time o(m*n),space o(n) 
    def calc1(self,logs):
        cntmap=[0]*101
        for i in logs:
            for y in range(i[0],i[1]):
                cntmap[y-1950] += 1
        return cntmap.index(max(cntmap))+1950
    # time o(m*n),space o(1) 
    def calc2(self,logs):
        maxcnt = 0
        maxyear = 0
        for i in range(1950,2051):
            s = 0
            for y in logs:
                if i >= y[0] and i < y[1]:
                    s+=1
                if (s > maxcnt):
                    maxcnt = s
                    maxyear = i
        return maxyear
    # time o(m+n)
    def calc3(self, logs):
        cntmap=[0]*101
        for i in logs:
            cntmap[i[0]-1950]+=1
            cntmap[i[1]-1950]-=1
        maxcnt = 0
        maxyear = 0
        curcnt = 0
        for i in range(101):
            curcnt += cntmap[i]
            if curcnt>maxcnt:
                maxcnt = curcnt
                maxyear =i+1950
        return maxyear
import random
import time
l = []
N = 100000
for _ in range(N):
    v0 = random.randint(1950,2049)
    v1 = random.randint(v0+1,2050)
    l.append([v0,v1])
# print (l)
s=Solution()
st = time.time()
print(s.calc1(l))
print(time.time()-st)
st = time.time()
print(s.calc2(l))
print(time.time()-st)
st = time.time()
print(s.calc3(l))
print(time.time()-st)


