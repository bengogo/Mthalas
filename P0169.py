class Solution:
    def majorityElement(self, nums) -> int:
        cnt = 0
        ans = None

        for num in nums:
            if cnt == 0:
                ans = num
            cnt += (1 if num == ans else -1)
        return ans



import random
l=[20]*5
for _ in range(random.randint(1,4)):
    l.append(random.randint(0,50))
random.shuffle(l)
print(l)
s=Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,3,1,1,4,1,1,5,1,1,6,2,2]))
print(s.majorityElement(l))