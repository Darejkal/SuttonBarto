import numpy as np
from numpy import typing as npt
head_chance=0.4
win_state=100
lose_state=0
vals=np.zeros((win_state-lose_state-1),dtype=float)
policy=np.zeros((win_state-lose_state-1),dtype=float)
def get_val(arr,state):
    if(state<=0):
        return 0
    elif(state>=100):
        return 1
    else:
        return arr[state-1]
def set_val(arr,state,val):
    if(state>0 and state<100):
        arr[state-1]=val
def valIter():
    for state in range(lose_state+1,win_state):
        for bet in range(0,state+1):
            temp=(head_chance*(get_val(vals,state+bet))+(1-head_chance)*(get_val(vals,state-bet)))
            if(temp>get_val(vals,state)):
                set_val(policy,state,bet)
                set_val(vals,state,temp)
for x in range(0,1000):
    valIter()
for x in range(0,np.shape(vals)[0]):
    print(f"state: {x+1}, chance {vals[x]:.1f}, policy: {policy[x]}")