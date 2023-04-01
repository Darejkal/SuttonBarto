import copy
MAPLENGTH=4
def iteravtive_availableAction(x,y):
    return [i for i in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)] if(i[0]>-1 and i[1]>-1 and i[0]<MAPLENGTH and i[1]<MAPLENGTH)]
def iterative(arr):
    for x in range(0,len(arr)):
        for y in range(0,len(arr[x])):
            if(arr[x][y]!=0):
                aval=iteravtive_availableAction(x,y)
                # Actions that are out of bound do not change the state.
                arr[x][y]=1/4*(-1+arr[x][y])*(4-len(aval))
                for i in aval:
                    arr[x][y]+=1/4*(-1+arr[i[0]][i[1]])
def outOfPlace(arr):
    old=copy.deepcopy(arr)
    for x in range(0,len(old)):
        for y in range(0,len(old[x])):
            if(old[x][y]!=0):
                aval=iteravtive_availableAction(x,y)
                # Actions that are out of bound do not change the state.
                arr[x][y]=1/4*(-1+old[x][y])*(4-len(aval))
                for i in aval:
                    arr[x][y]+=1/4*(-1+old[i[0]][i[1]])
def iterImprove(arr):
    for x in range(0,len(arr)):
        for y in range(0,len(arr[x])):
            if(arr[x][y]!=0):
                arr[x][y]=max(arr[x][y],*[(-1+arr[i[0]][i[1]]) for i in iteravtive_availableAction(x,y)])
def outOfPlaceImprove(arr):
    old=copy.deepcopy(arr)
    for x in range(0,len(old)):
        for y in range(0,len(old[x])):
            if(old[x][y]!=0):
                arr[x][y]=max(old[x][y],*[(-1+old[i[0]][i[1]]) for i in iteravtive_availableAction(x,y)])
a=[]
for x in range(0,MAPLENGTH):
    a.append([])
    for y in range(0,MAPLENGTH):
        a[x].append(-1.0)
a[0][0]=0.0
a[MAPLENGTH-1][MAPLENGTH-1]=0.0
for x in a:
    for y in x:
        print(f"{y:.1f}",end=" ")
    print()
print()
for i in range(0,1000):
    outOfPlace(a)
for i in range (0,1000):
    outOfPlaceImprove(a)
for x in a:
    for y in x:
        print(f"{y:.1f}",end=" ")
    print()
print()
