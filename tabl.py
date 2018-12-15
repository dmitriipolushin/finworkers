import random
import math as m
import player
def LevelCount(Lvl):
    Count=0
    Count=random.randint(1,12)
    if (2<=Lvl<=4):
        if (Count in range(2,5,1)):
            Lvl+=4
        elif (5<=Count<=8):
            Lvl+=5
        elif (9<=Count<=11):
            Lvl+=1
        elif (Count==12):
            Lvl+=2
        else: Lvl+=3
    if Lvl==1:
        if (5<=Count<=8):
            Lvl=2
        elif (9<=Count<=10):
            Lvl=3
        elif (Count==12):
            Lvl=5
        elif (Count==11):
            Lvl=4
    if Lvl==5:
        if (1<=Count<=4):
            Lvl=4
        elif (9<=Count<=10):
            Lvl=3
        elif (Count==12):
            Lvl=2
        elif (Count==11):
            Lvl=1
    if Lvl>5: Lvl-=5
    print('Уровень=', Lvl)
    return Lvl
