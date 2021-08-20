MAXN = 10
tree = [0]*MAXN
def lowbit(x):
    return x & (-x)
def update(i,x):
    pos = i
    while pos < MAXN:
        tree[pos] += x
        pos += lowbit(pos)
def query(n):
    ans = 0
    pos = n
    while pos > 0:
        ans += tree[pos]
        pos -= lowbit(pos)
    return ans
def queryab(a,b):
    return query(b)-query(a-1)

import time

#----------------------------------------------------
# 求局部和
#----------------------------------------------------
def calcsum():
    s1=[0]*MAXN
    st = time.time()
    for i in range(1,MAXN):
        update(i,2*i)
    # print(tree)
    for i in range(1,MAXN):
        s1[i]=query(i)
        # queryab(i,i)
    print(time.time()-st)

    l=[i*2 for i in range(MAXN)]
    st = time.time()
    # print(tree)
    for i in range(1,MAXN):
        s = sum(l[:i+1])
    print(time.time()-st)
# calcsum()

#----------------------------------------------------
# 求输入的逆序对
#----------------------------------------------------
def revsPair():
    b = [[0,0]]
    n = int(input())
    for i in range(1,n+1):
        t = int(input())
        b.append([t,i])
    b.sort()
    print(b[1:])
    a = [0]*len(b)
    for i in range(1,n+1):
        a[b[i][1]]=i
    print(a)
    sum = 0
    for i in range(1,n+1):
        sum += query(a[i])
        update(a[i],1)
    sum = n*(n-1)//2-sum
    print(sum)
# revsPair()


#---------------------------------------------------
class gmap():
    def __init__(self,m,n):
        self.mat = [[0]*(n+1) for _ in range(m+1)]
        self.p=[0]*(n+1)
        self.vis=[0]*(n+1)
    def add(self,u,v,w=1):
        self.mat[u][v]=w
#         self.mat[v][u]=w
    def match(self,i):
        for j in range(1,len(self.mat[0])):
            if self.mat[i][j] and self.vis[j]==0:
                self.vis[j]=1
                if self.p[j]==0 or self.match(self.p[j]):
                    self.p[j]=i
                    return True
        return False
def maxPair():        
    M,N = 6,7
    gm = gmap(M,N)

    edges =[[1,1],[1,2],[1,4],[2,2],[2,5],[3,1],[3,4],[3,7],[4,3],[4,6],[5,4],[6,4]]
    for i in edges:
        gm.add(i[0],i[1])
    print(gm.mat)

    cnt = 0
    for i in range(1,M+1):
        gm.vis=[0]*(N+1)
        if gm.match(i):
            print(i,gm.p)
            cnt+=1
    # print(gm.p)
    print(cnt)
# maxPair()

#--------------------------------------------------------------
class Trie:
    class trieNode:
        def __init__(self):
            self.isStr = False
            self.next = [None]*26
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.trieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tr = self.root
        for v in word:
            if tr.next[ord(v)-ord('a')] == None:
                tr.next[ord(v)-ord('a')] = Trie.trieNode()
            tr = tr.next[ord(v)-ord('a')]
        tr.isStr = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tr = self.root
        for v in word:
            if tr is None or tr.next[ord(v)-ord('a')] == None:
                return False
            tr = tr.next[ord(v)-ord('a')]
        return (tr is not None) and tr.isStr == True
         

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tr = self.root
        for v in prefix:
            if tr is None or tr.next[ord(v)-ord('a')] == None:
                return False
            tr = tr.next[ord(v)-ord('a')]
        return True
def testTrie():
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)
    obj = Trie()
    obj.insert('append')
    obj.insert('bless')
    obj.insert('abandon')
    print(obj.search('appenda'))
    print(obj.startsWith('ab'))
# testTrie()

#------------------------------------------------------------
import copy
class Solution:
    def findWords(self, board, words):
        ans = []
        m,n = len(board),len(board[0])
        orgboardmap={}
        for i in range(m):
            for j in range(n):
                if board[i][j] in orgboardmap:
                    orgboardmap[board[i][j]].append([i,j])
                else:
                    orgboardmap[board[i][j]] = [[i,j]]
        for w in words:
            prev = [-1,-1]
            finded = True
            boardmap = copy.deepcopy(orgboardmap)
            for wv in w:
                if wv not in boardmap:
                    finded = False
                    break
                cur = boardmap[wv]
                if prev == [-1,-1]:
                    prev = cur
                else:
                    tempcur = []
                    tii = []
                    for  posprev in prev:
                        for i,poscur in enumerate(cur):
                            if (abs(poscur[0]-posprev[0])+abs(poscur[1]-posprev[1])==1):
                                tempcur.append(poscur)
                                tii.append(i)
                    if len(tempcur)==0:
                        finded = False
                        break
                    else:
                        for i in tii[::-1]:
                            cur.pop(i)
                        prev = tempcur
            if (finded):
                ans.append(w)
        return ans
def testfindWords():
    s=Solution()
    # b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    # ws = ["oath","pea","eat","rain"]
    b=[['a','a']]
    ws = ['aa','a']
    print(s.findWords(b,ws))
testfindWords()