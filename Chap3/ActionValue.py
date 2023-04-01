import heapq as hq
import random as rd
n=int(input())
steps=int(input())
times=int(input())
omega=int(input())
a=[]
for i in range(0,n):
    taction=input()
    treward=input()
    # the treward here does not vary, which is a limitation
    a.append((0,taction,int(treward)))
hq.heapify(a)
for x in range(0,times):
    reward=0
    for y in range (0,steps):
        if rd.choices([True,False],weights=[omega,1-omega],k=1):
            actNo=rd.randrange(0,len(a))
            reward=reward+a[actNo][2]
            a[actNo][0]=(a[actNo][2]+a[actNo][0])/2
            hq.heapify(a)
        else:
            act=hq.heappop(a)
            reward=reward+act[2]
            # This is not the expectation, but the algo adaptation to changes will be better 
            # And we don't have to store the times action A is used.
            # Perhaps apply an ratio would modify the speed to the like of coder.
            act[0]=(act[2]+act[0])/2
            hq.heappush(a,act)






