class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def binsearch(row,t):
            l,r = 0,len(row)-1
            while l<=r:
                mid = (l+r)//2
                if (row[mid] == t):
                    return mid
                elif row[mid] > t:
                    r = mid-1
                else:
                    l = mid+1
            return l
        m,n = len(matrix),len(matrix[0])
        col0 = [matrix[i][0]  for i in range(m)]
        col1 = [matrix[i][-1]  for i in range(m)]
        maxcol = binsearch(col0,target)
        # mincol = binsearch(col1,target)
        # print(maxcol,mincol)
        if maxcol<m and  target == matrix[maxcol][0]:
            return True
        for i in range(maxcol):
            ans = binsearch(matrix[i],target)
            if ans<n and  target == matrix[i][ans]:
                return True
        return False

import random
l = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
t = 21

s=Solution()
for t in range(31):
    print(t,s.searchMatrix(l,t))