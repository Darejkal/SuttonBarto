# This uses the last drawn class as state instead of the Player sum (as in the book).
# There is a wrong assumption in the book that usable card (Ace that can be converted to 11 without busting) should always be counted as 11.
# However, the rate of drawing more than 2 Aces in an episode is kinda rare, so the assumption might not have a great impact on the policy.
import numpy as np
def cardDraw():
    drawn=np.random.randint(low=1,high=14)
    if(drawn>10 and drawn<14):
        drawn=10
    return drawn
def episodeGen():
    player=[cardDraw()]
    p=player[-1]
    pHasAce=False
    pStick=False
    dealer=[cardDraw()]
    d=dealer[-1]
    dStick=False
    dHasAce=False
    while(not pStick or not dStick):
        if not pStick:
            player.append(cardDraw())
            pHasAce=pHasAce or player[-1]==1
            p+=player[-1]
            if(p>21):
                break
            # elif(p== 21 or np.random.randint(low=2)==1):
            elif(p>=20 or (pHasAce and p+10>=20 and p+10<21)):
                pStick=True
                if(pHasAce and p+10<=21):
                    p+=10 # can only convert one ace before going bust.
        if not dStick:
            dealer.append(cardDraw())
            dHasAce=dHasAce or dealer[-1]==1
            d+=dealer[-1]
            if(d>21):
                break
            elif(d>=17 or (dHasAce and d+10>=17 and d+10<=21)):
                dStick=True
                if(dHasAce and d+10<=21):
                    d+=10 # can only convert one ace before going bust.
    return [(player,p),(dealer,d)]
# episode=episodeGen()
# for x in episode:
#     for y in x:
#         print(y)
# exit()
states=[]
for x in range(0,10):
    states.append([])
    for y in range(0,10):
        states[x].append(0.0)
visited=[]
for x in range(0,10):
    visited.append([])
    for y in range(0,10):
        visited[x].append(0)
def gameResult(player,dealer):
    if dealer>21 or (player<=21 and dealer<player):
        return 1
    elif player<=21 and dealer==player:
        return 0
    return -1
def firstVistMC():
    global states,visited
    justVisited=np.zeros((10,10))
    episode=episodeGen()
    #Discount=0 and Result=0 for all other steps besides the final one so state values stay the same as the final's.
    val=float(gameResult(episode[0][1],episode[1][1])) 
    dealerShown=episode[1][0][0]
    for x in reversed(episode[0][0]):
        if(justVisited[dealerShown-1][x-1]==0):
            states[dealerShown-1][x-1]=(states[dealerShown-1][x-1]*visited[dealerShown-1][x-1]+val)/(visited[dealerShown-1][x-1]+1)
            visited[dealerShown-1][x-1]+=1
            justVisited[dealerShown-1][x-1]=1
for x in range(0,500000):
    firstVistMC()
for x in states:
    for y in x:
        print(f"{y:.1f}",end=" ")
    print()