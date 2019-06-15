import player
import costs
import tabl
import Esm
import Egp
import buildings
import production
import math as m
import loseAndWin
import loans
import capital
print('Добро пожаловать в игру финансовые воротилы!')
mes=1
Level=3
print('Начало игры')
player.players()
#windows.showTable()
while mes < 13:
    print('Текущий месяц = ', mes)
    costs.monthlyCosts()
    #windows.showTable()
    starshiy=m.fmod(mes, player.CurNumOfGamers)
    Level=tabl.LevelCount(Level)
    Esm.AcquisitionOfEsm(Level)
    production.productionEgp()
    Egp.AcquisitionOfEgp(Level)
    for ActualGamer in range(player.CurNumOfGamers):
        buildings.buildings(ActualGamer)
    capital.capitalFunc(Level)
    loans.LoansPercents()
    loans.LoansRepayment(mes)
    loans.LoansFunc(Level,mes)
    capital.capitalFunc(Level)
    loseAndWin.loser()
    if len(player.qplayers) == 1:
        break
    mes+=1
capital.capitalFunc(Level)
loseAndWin.winner()