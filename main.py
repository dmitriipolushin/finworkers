import player
import costs
import tabl
import Esm
import math as m
print('Добро пожаловать в игру финансовые воротилы!')
mes=1
tabl.Level=3
print('Начало игры')
player.players()
while mes < 13:
    print('Текущий месяц = ', mes)
    costs.monthlyCosts()
    starshiy=m.fmod(mes,player.curNumOfGamers)
    Esm.AcquisitionOfEsm(tabl.Level)
    tabl.Level=tabl.LevelCount(tabl.Level)
    



    mes+=1 
