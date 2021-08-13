class Solution:
    def searchRange(self, nums, target: int):
        def bsearche_ge(flag):
            l,r = 0,len(nums)-1
            ans = len(nums)
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>target or (flag and nums[mid]>=target):
                    r = mid-1
                    ans = mid
                else:
                    l = mid+1
            return ans

        left = bsearche_ge(True)
        right = bsearche_ge(False)-1
        if (left<=right and right < len(nums) 
            and nums[left]==target and nums[right]==target):
            return [left,right]
        return [-1,-1]


import random
s = Solution()

l =[random.randint(1,20) for _ in range(30)]
l.sort()

t = random.randint(1,30)
print(l)
print(t)
print(s.searchRange(l,t))