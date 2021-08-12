class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        cnt = 0
        st = len(num)-2
        while cnt < k:
            while st >= 0:
                partnum = num[st:]
                partset = sorted(set(partnum))
                idx = partset.index(partnum[0])
                curcnt = (len(partset)-1-idx) * (len(partset)-1)
                if (cnt+curcnt) >= k:
                    break
                cnt+=curcnt
