class Solution:
    def minSpeedOnTime(self, dist, hour) -> int:
        def getSpeed(dist,hour):
            sp1 = dist/hour
            if abs(sp1-dist//hour) < 1e-6:
                return int(sp1)
            else:
                return int(sp1)+1
        n = len(dist)
        sumdist = sum(dist)
        if hour <= n-1:
            return -1
        if hour >= sumdist:
            return 1
        lasthour = hour-(n-1)
        if 1.0 > lasthour > 0.0:
            sp = getSpeed(dist[-1],lasthour)
            sp = max(sp,max(dist))
        else:
            sp = getSpeed(sumdist,hour)
        
        cursum = 0.0
        for i in dist[:-1]:
            cursum+=getSpeed(i,sp)
        cursum+=dist[-1]/sp
        if cursum<=hour:
            return sp
        return -1

s=Solution()
print(s.minSpeedOnTime([2,1,5,4,4,3,2,9,2,10],75.12))
# print(s.minSpeedOnTime([1,1,100000],2.01))
# print(s.minSpeedOnTime([1,3,2],6))
# print(s.minSpeedOnTime([1,3,2],2.7))
# print(s.minSpeedOnTime([1,3,2],1.9))
        