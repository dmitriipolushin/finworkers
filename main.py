import player
import costs
import tabl
import Esm
import Egp
import buildings
import production
import windows
import math as m
print('Добро пожаловать в игру финансовые воротилы!')
mes=1
tabl.Level=3
print('Начало игры')
player.players()
#windows.showTable()
while mes < 13:
    print('Текущий месяц = ', mes)
    costs.monthlyCosts()
    windows.showTable()
    starshiy=m.fmod(mes, player.CurNumOfGamers)
    tabl.Level=tabl.LevelCount(tabl.Level)
    Esm.AcquisitionOfEsm(tabl.Level)
    production.productionEgp()
    Egp.AcquisitionOfEgp(tabl.Level)
    buildings.buildings()
    mes+=1