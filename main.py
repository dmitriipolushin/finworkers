import player
import costs
print('Добро пожаловать в игру финансовые воротилы!')
mes=1
Level=3
print('Начало игры')
while mes<13:
    print('Текущий месяц = ', mes)
    starshiy=m.fmod(mes,CurNumOfGamers)
    AcquisitionOfEsm (Level)
    Level=LevelCount(Level)
    mes+=1
for i in range(len(players)):
    costs.monthlyCosts(players[i])
print(players[0]['money']) 
