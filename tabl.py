# -*- coding: utf-8 -*-
import random
import math as m

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

print('Сколько игроков? ')
CurNumOfGamers=int(input())
a=[[CurNumOfGamers,800,3*CurNumOfGamers,6500],
  [m.trunc(1.5*CurNumOfGamers),650,m.trunc(2.5*CurNumOfGamers),6000],
  [2*CurNumOfGamers,500,2*CurNumOfGamers,5500],
  [m.trunc(2.5*CurNumOfGamers),400,m.trunc(1.5*CurNumOfGamers),5000],
  [3*CurNumOfGamers,300,CurNumOfGamers,4500]]
mes=1
Lvl=3
print('Начало игры')
while mes<13:
    print('Текущий месяц = ', mes)
    starshiy=m.fmod(mes,CurNumOfGamers)
    Lvl=LevelCount(Lvl)
    mes+=1