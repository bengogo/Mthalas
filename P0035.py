# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        def bsearche():
            l,r = 0,len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return l
        return bsearche()

import random
s = Solution()
l = list(range(1,10))
for i in range(11):
    print(s.searchInsert(l,i))