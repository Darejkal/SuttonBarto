#DONE
import numpy as np
import matplotlib.pyplot as plt
import math
#environment
NUMBER_OF_ACTION=2 #left&right
TERMINATION_CHANCE=np.array([0.1,1],dtype=float)
TERMINATION_REWARD=float(1) #for termination
RESET_REWARD=float(0) # for returning to s
#policy
BEHAVIOUR=np.array([0.5,0.5],dtype=float)
TARGET=np.array([1,0],dtype=float)
POSS=np.array([TARGET[i]/BEHAVIOUR[i] for i in range(NUMBER_OF_ACTION)],dtype=float)
def gen():
    acts=[]
    terminated=False
    while(not terminated):
        choice=np.random.choice(a=np.arange(NUMBER_OF_ACTION),p=BEHAVIOUR)
        acts.append(choice)
        terminated=np.random.choice(a=[True,False],p=[TERMINATION_CHANCE[choice],1-TERMINATION_CHANCE[choice]])
    return acts
states=np.zeros(NUMBER_OF_ACTION,dtype=float)
weights=np.zeros(NUMBER_OF_ACTION,dtype=float)
def weighted_EVope(loop=1,discount=1):
    global states,weights
    for _ in range(loop):
        acts=list(gen())
        val=TERMINATION_REWARD
        poss=POSS[acts[-1]]
        if weights[acts[-1]]+poss:
            states[acts[-1]]=(states[acts[-1]]*weights[acts[-1]]+val*poss)/(weights[acts[-1]]+poss)
        weights[acts[-1]]+=poss
        for x in reversed(acts[0:-1]):
            val=RESET_REWARD+discount*val
            poss*=POSS[acts[x]]
            if weights[x]+poss!=0:
                states[x]=(states[x]*weights[x]+val*poss)/(weights[x]+poss)
            weights[x]+=poss

ordinary_states=np.zeros(NUMBER_OF_ACTION,dtype=float)
visited=np.zeros(NUMBER_OF_ACTION,dtype=float)
def ordinary_EVope(loop=1,discount=1):
    global ordinary_states,visited
    for _ in range(loop):
        acts=gen()
        val=TERMINATION_REWARD
        poss=POSS[acts[-1]]
        ordinary_states[acts[-1]]=(ordinary_states[acts[-1]]*visited[acts[-1]]+val*poss)/(visited[acts[-1]]+1)
        visited[acts[-1]]+=1
        for x in reversed(acts[0:-1]):
            val=RESET_REWARD+discount*val
            poss*=POSS[acts[x]]
            ordinary_states[x]=(ordinary_states[x]*visited[x]+val*poss)/(visited[x]+1)
            visited[x]+=1
def ordinary_FVope(loop=1,discount=1):
    global ordinary_states,visited
    for _ in range(loop):
        acts=gen()
        returns=np.zeros(len(acts),dtype=float)
        returns[-1]=TERMINATION_REWARD
        poss=np.zeros(len(acts),dtype=float)
        poss[-1]=POSS[acts[-1]]
        for i in reversed(range(len(acts)-1)):
            returns[i]=returns[i+1]*discount+RESET_REWARD
            poss[i]=poss[i+1]*POSS[acts[i]]
        history=dict()
        for i in range(len(acts)):
            if acts[i] not in history:
                history[acts[i]]=1
                ordinary_states[acts[i]]=(ordinary_states[acts[i]]*visited[acts[i]]+returns[i]*poss[i])/(visited[acts[i]]+1)
                visited[acts[i]]+=1
for y in range(0,10):
    xAxis=[]
    yAxis=[]
    for x in range(1,2000):
        l=1
        weighted_EVope(loop=l)
        xAxis.append(x*l)
        # Please print states if you used weighted methods and ordinary for ordinary ones.
        yAxis.append(states[0])
        plt.plot(xAxis,yAxis,"-")
plt.show()



        

