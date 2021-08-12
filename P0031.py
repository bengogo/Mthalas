class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >=0 and nums[i]>=nums[i+1]:
            i-=1
        if (i>=0):
            j = len(nums)-1
            while j>i and nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=list(reversed(nums[i+1:]))

# [3,3,4,2,5]
# [3,1,2,2,4,5]
s = Solution()

l=[3,3,2,5,4]
for k in range(4):
    s.nextPermutation(l)
    print(l)

l=[2,5,4,3,2,1]
s.nextPermutation(l)
print(l)

l=[7,6,5]
s.nextPermutation(l)
print(l)
