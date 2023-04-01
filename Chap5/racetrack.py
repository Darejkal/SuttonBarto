import numpy as np
<<<<<<< HEAD
import copy
MAP_SIZE=(100,100)
START=[(0,MAP_SIZE[1]-1),(MAP_SIZE[0]/3,MAP_SIZE[1]-1)]
STEP=(int(MAP_SIZE[0]/3),int(MAP_SIZE[1]/3))
END=[(MAP_SIZE[1]-1,0),(MAP_SIZE[1]-1,MAP_SIZE[0]/3)]
def onLoad():
    states=np.ones((MAP_SIZE[0],MAP_SIZE[1],min(MAP_SIZE[0],MAP_SIZE[1])))
    for x in range(min(START[0][0],START[1][0]),max(START[0][0],START[1][0])+1):
        for y in range(min(START[0][1],START[1][1]),max(START[0][1],START[1][1])+1):
            states[x][y]=-1
    for x in range(min(END[0][0],END[1][0]),max(END[0][0],END[1][0])+1):
        for y in range(min(END[0][1],END[1][1]),max(END[0][1],END[1][1])+1):
            states[x][y]=0
    
def gen():
    global MAP_SIZE,START,END
    map=np.ones(MAP_SIZE)
    for x in range(min(START[0][0],START[1][0]),max(START[0][0],START[1][0])+1):
        for y in range(min(START[0][1],START[1][1]),max(START[0][1],START[1][1])+1):
            map[x][y]=-1
    for x in range(min(END[0][0],END[1][0]),max(END[0][0],END[1][0])+1):
        for y in range(min(END[0][1],END[1][1]),max(END[0][1],END[1][1])+1):
            map[x][y]=0
    #border_gen()
    policy=        
    
=======

>>>>>>> 38618b9000a88d1133d243a12991156a72759d9a

