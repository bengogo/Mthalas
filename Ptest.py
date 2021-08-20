class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        ans =[]
        while i < m and j< n:
            if (nums1[i]<=nums2[j]):
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        ans.extend(nums1[i:m])
        ans.extend(nums2[j:n])
        nums1[:]=ans[:]
    def ispa(self,s):
        l,r = 0,len(s)-1
        while(l<r):
            if (s[l]!=s[r]):
                return False
        return True
    def wordBreak(self, s, wordDict):
        dmin = 10**5
        dmax = 0
        for w in wordDict:
            if len(w)<dmin:
                dmin = len(w)
            if len(w)>dmax:
                dmax = len(w)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        cursec=[]
        for i in range(n):
            for j in range(i+dmin,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
                    cursec.append([i,j,0])
        print(cursec)
        if (dp[-1]):
            setences = [[0,-1]]
            stindex = 0
            ans =[]
            while len(setences) > 0:
                if setences[-1][0] == n:
                    cursetc = ''
                    for i in setences[1:]:
                        cursetc+=s[cursec[i[1]][0]:cursec[i[1]][1]]+' '
                    cursetc = cursetc[:-1]
                    ans.append(cursetc)

                    resi = setences.pop()
                    stindex=resi[1]+1
                    cursec[resi[1]][2] = 0
                else:
                    findnext = 0
                    for i in range(stindex,len(cursec)):
                        if cursec[i][0] == setences[-1][0] and cursec[i][2]==0:
                            cursec[i][2] = 1
                            setences.append([cursec[i][1],i])
                            findnext = 1
                    if findnext == 0:
                        resi = setences.pop()
                        cursec[resi[1]][2] = 0
                        stindex=resi[1]+1
                
            return ans
        else:
            return []
       

import random
s=Solution()
# l1 = [1,23,0,0,0]
# l2 = [1,2,3,4]
# s.merge(l1,2,l2,4)
# print(l1)
st = "catsanddog"



wordDict = ["cat","cats","and","sand","dog"]
print(s.wordBreak(st,wordDict))
