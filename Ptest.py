import random
import time
from functools import reduce
def fadd(x1,x2):
    return x1+x2
l = [random.randint(1,1000) for _ in range(10**6)]
pre=[]
sumval = 0
st=time.time()
for i,m in enumerate(l):
    sumval += m
    pre.append(sumval)
print(time.time()-st)
pre =[l[0]]
st=time.time()
# pre = sum(l)
for i in range(1,len(l)):
    pre.append(sum(l[:i]))
print(time.time()-st)
