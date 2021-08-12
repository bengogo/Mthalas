class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        lenof0,lenof1 = 0,0
        maxof0,maxof1 = 0,0
        for i in s:
            if i=='0':
                lenof0+=1
                if lenof1 > maxof1:
                    maxof1 = lenof1
                lenof1=0
            else:
                lenof1+=1
                if lenof0 > maxof0:
                    maxof0 = lenof0
                lenof0=0
        if lenof0 > maxof0:
            maxof0 = lenof0
        if lenof1 > maxof1:
            maxof1 = lenof1   

        return maxof1>maxof0
    def checkZeroOnes1(self, s: str) -> bool:
        l=[0,0]
        i = 0
        while i<len(s):
            j=i+1
            while j<len(s) and s[j]==s[i]:
                j+=1
            if j-i>l[int(s[i])]:
                l[int(s[i])]=j-i
            i=j
        return l[1]>l[0]


s=Solution()
print(s.checkZeroOnes1("110100010"))
print(s.checkZeroOnes1("11110000"))