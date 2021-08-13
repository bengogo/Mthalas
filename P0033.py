class Solution:
    def search(self, nums, target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1




s=Solution()
l=list(range(10))
l=l[4:]+l[0:4]
print(l)
for i in range(11):
    print(i,s.search(l,i))
