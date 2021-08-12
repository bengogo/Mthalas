'''
/***************************************************************************************************** 
 *
 * You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.
 * 
 * A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i 
 * <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.
 * 
 * Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.
 * 
 * An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
 * 
 * Example 1:
 * 
 * Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
 * Output: 2
 * Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
 * The maximum distance is 2 with pair (2,4).
 * 
 * Example 2:
 * 
 * Input: nums1 = [2,2,2], nums2 = [10,10,1]
 * Output: 1
 * Explanation: The valid pairs are (0,0), (0,1), and (1,1).
 * The maximum distance is 1 with pair (0,1).
 * 
 * Example 3:
 * 
 * Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
 * Output: 2
 * Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
 * The maximum distance is 2 with pair (2,4).
 * 
 * Example 4:
 * 
 * Input: nums1 = [5,4], nums2 = [3,2]
 * Output: 0
 * Explanation: There are no valid pairs, so return 0.
 * 
 * Constraints:
 * 
 * 	1 <= nums1.length <= 10^5
 * 	1 <= nums2.length <= 10^5
 * 	1 <= nums1[i], nums2[j] <= 10^5
 * 	Both nums1 and nums2 are non-increasing.
 ******************************************************************************************************/
'''

class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        def findlessindex(nums,target):
            left,right = 0,len(nums)-1
            while left<right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    left = mid+1
                else:
                    right = mid
            if (nums[left]<target):
                return left - 1
            return left
        n1,n2=len(nums1),len(nums2)
        maxlen = 0
        # for i,v in enumerate(nums1):
        #     if i >= n2:
        #         break
        #     if (nums2[i]<v):
        #         continue
        #     ni = findlessindex(nums2[i:],v)
        #     maxlen = max(ni,maxlen)
        i,j = 0,0
        while i<n1 and j < n2:
            if (nums1[i] > nums2[j]):
                i+=1
            else:
                maxlen = max(maxlen,j-i)
                j+=1
        return maxlen

  
import random
import time
N = 10
nums1 = [random.randint(1,10**5) for _ in range(N)]
nums1.sort()
nums2 = [random.randint(1,10**5) for _ in range(N)]
nums2.sort()
nums1 = nums1[::-1]
nums2 = nums2[::-1]
print(nums1)
print(nums2)
s=Solution()
st = time.time()
print(s.maxDistance(nums1,nums2))
print(time.time()-st)