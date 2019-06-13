import numpy as np
import player
value = np.zeros((10), dtype=int)
quantity = np.zeros_like(value)
numbersmix = np.zeros_like(value)
def mixEsm():
    for ActualGamer in range(player.CurNumOfGamers-1): #процедура сортировки заявок 
        for d in range(player.CurNumOfGamers-ActualGamer-1):
            if value[d]<value[d+1]:
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d]
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
    for ActualGamer in range(player.CurNumOfGamers):
        if (quantity[ActualGamer]==0):
            print(ActualGamer+1,'. ','Игрок ',player.qplayers[ActualGamer]['name'],' не делал заявки ')
        else:
            print(ActualGamer+1,'. ','Заявка игрока ',numbersmix[ActualGamer]+1,' величиной ',value[ActualGamer],' за одну ЕСМ')
def satisfactionEsm(rmngESM): #процедура удовлетворения заявок
    for ActualGamer in range(player.CurNumOfGamers):
        if ((rmngESM>=quantity[ActualGamer]) and (rmngESM!=0)): #проверка поданой заявки. Если продается есм больше, чем покупается
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*quantity[ActualGamer]
            player.qplayers[numbersmix[ActualGamer]]['esm']+= quantity[ActualGamer]
            print(' Игрок ',numbersmix[ActualGamer]+1,' получает ',quantity[ActualGamer],' ЕСМ')
            rmngESM-=quantity[ActualGamer]
        elif((rmngESM<=quantity[ActualGamer]) and (rmngESM!=0)): # Если есм осталось меньше, чем нужно игроку
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*rmngESM
            player.qplayers[numbersmix[ActualGamer]]['esm']+= rmngESM
            print(' Игрок ',numbersmix[ActualGamer]+1,' получает ',rmngESM,' ЕСМ')
            rmngESM=0
        else: # если есм не соталось
            print(' Все ЕСМ были раскуплены ')
            print('оставшиеся деньги игрока ',numbersmix[ActualGamer]+1,' = ',player.qplayers[numbersmix[ActualGamer]]['money'])
def mixEgp():
    for ActualGamer in range(player.CurNumOfGamers-1): #процедура сортировки заявок 
        for d in range(player.CurNumOfGamers-ActualGamer-1):
            if value[d]>value[d+1]:
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d]
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
    for ActualGamer in range(player.CurNumOfGamers):
        if (quantity[ActualGamer]==0):
            print(ActualGamer+1,'. ','Игрок ',numbersmix[ActualGamer]+1,' не делал заявки ')
        else:
            print(ActualGamer+1,'. ','Заявка игрока ',numbersmix[ActualGamer]+1,' величиной ',value[ActualGamer],' за одну ЕГП')

def satisfactionEgp(rmngEGP): #процедура удовлетворения заявок егп
    for ActualGamer in range(player.CurNumOfGamers):
        if ((rmngEGP>=quantity[ActualGamer]) and (rmngEGP!=0)): #проверка поданой заявки. Если прокупается егп больше, чем продается
            player.qplayers[numbersmix[ActualGamer]]['money']+=value[ActualGamer]*quantity[ActualGamer]
            player.qplayers[numbersmix[ActualGamer]]['egp']-= quantity[ActualGamer]
            print('Прибыль игрока ',numbersmix[ActualGamer]+1,' = ',value[ActualGamer]*quantity[ActualGamer])
            rmngEGP-=quantity[ActualGamer];
        elif((rmngEGP<=quantity[ActualGamer]) and (rmngEGP!=0)): # Если егп покупается меньше, чем продает игроком
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*rmngEGP
            player.qplayers[numbersmix[ActualGamer]]['egp']-= rmngEGP
            print('Прибыль игрока ',numbersmix[ActualGamer]+1,' = ',value[ActualGamer]*rmngEGP)
            rmngEGP=0
        else: # если было скупленнно нужное кол-во егп
            print('   Заказчик закупил максимальное кол-во ЕГП ')
        print('Деньги игрока ',numbersmix[ActualGamer]+1,' c учетом прибыли = ',player.qplayers[numbersmix[ActualGamer]]['money'])