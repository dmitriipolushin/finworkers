import random
import math as m
import player
def LevelCount(Lvl):
    print('Уровень=', Lvl)
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
    if Lvl>5: Lvl-=5;
    return Lvl
a=[[player.CurNumOfGamers,800,3*player.CurNumOfGamers,6500],
  [m.trunc(1.5*player.CurNumOfGamers),650,m.trunc(2.5*player.CurNumOfGamers),6000],
  [2*player.CurNumOfGamers,500,2*player.CurNumOfGamers,5500],
  [m.trunc(2.5*player.CurNumOfGamers),400,m.trunc(1.5*player.CurNumOfGamers),5000],
  [3*player.CurNumOfGamers,300,player.CurNumOfGamers,4500]]