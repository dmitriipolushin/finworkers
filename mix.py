import numpy as np
import player
value = np.zeros((10), dtype=int)
quantity = np.zeros_like(value)
numbersmix = np.zeros_like(value)
def mixEsm(s):
    for ActualGamer in range(player.CurNumOfGamers-1): #процедура сортировки заявок 
        for d in range(player.CurNumOfGamers-ActualGamer-1):
            if value[d]<value[d+1]:
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d] #сортировка порядка
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
        for d in range(player.CurNumOfGamers-ActualGamer-1): #Сортировка одинаковых заявок по старшенству заявителя
            if value[d]==value[d+1] and (abs(numbersmix[d]-s) > abs(numbersmix[d+1]-s)):
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d] #сортировка порядка
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
    for ActualGamer in range(player.CurNumOfGamers):
        if (quantity[ActualGamer]==0):
            print(ActualGamer+1,'. ','Игрок ',player.qplayers[ActualGamer]['name'],' не делал заявки ')
        else:
            print(ActualGamer+1,'. ','Заявка игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' величиной ',value[ActualGamer],' за одну ЕСМ')
def satisfactionEsm(rmngESM): #процедура удовлетворения заявок
    for ActualGamer in range(player.CurNumOfGamers):
        if ((rmngESM>=quantity[ActualGamer]) and (rmngESM!=0)): #проверка поданой заявки. Если продается есм больше, чем покупается
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*quantity[ActualGamer]
            player.qplayers[numbersmix[ActualGamer]]['esm']+= quantity[ActualGamer]
            print(' Игрок ',player.qplayers[numbersmix[ActualGamer]]['name'],' получает ',quantity[ActualGamer],' ЕСМ')
            rmngESM-=quantity[ActualGamer]
        elif((rmngESM<=quantity[ActualGamer]) and (rmngESM!=0)): # Если есм осталось меньше, чем нужно игроку
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*rmngESM
            player.qplayers[numbersmix[ActualGamer]]['esm']+= rmngESM
            print(' Игрок ',player.qplayers[numbersmix[ActualGamer]]['name'],' получает ',rmngESM,' ЕСМ')
            rmngESM=0
        else: # если есм не соталось
            print(' Все ЕСМ были раскуплены ')
            print('оставшиеся деньги игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' = ',player.qplayers[numbersmix[ActualGamer]]['money'])
def mixEgp(s):
    for ActualGamer in range(player.CurNumOfGamers-1): #процедура сортировки заявок 
        for d in range(player.CurNumOfGamers-ActualGamer-1):
            if value[d]>value[d+1]:
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d] #Сортировка порядка
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
        for d in range(player.CurNumOfGamers-ActualGamer-1): #Сортировка одинаковых заявок по старшенству заявителя
            if value[d]==value[d+1] and (abs(numbersmix[d]-s) > abs(numbersmix[d+1]-s)):
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmix[d] #Сортировка порядка
                numbersmix[d]= numbersmix[d+1]
                numbersmix[d+1]=xx
    for ActualGamer in range(player.CurNumOfGamers):
        if (quantity[ActualGamer]==0):
            print(ActualGamer+1,'. ','Игрок ',player.qplayers[numbersmix[ActualGamer]]['name'],' не делал заявки ')
        else:
            print(ActualGamer+1,'. ','Заявка игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' величиной ',value[ActualGamer],' за одну ЕГП')

def satisfactionEgp(rmngEGP): #процедура удовлетворения заявок егп
    for ActualGamer in range(player.CurNumOfGamers):
        if ((rmngEGP>=quantity[ActualGamer]) and (rmngEGP!=0)): #проверка поданой заявки. Если прокупается егп больше, чем продается
            player.qplayers[numbersmix[ActualGamer]]['money']+=value[ActualGamer]*quantity[ActualGamer]
            player.qplayers[numbersmix[ActualGamer]]['egp']-= quantity[ActualGamer]
            print('Прибыль игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' = ',value[ActualGamer]*quantity[ActualGamer])
            rmngEGP-=quantity[ActualGamer];
        elif((rmngEGP<=quantity[ActualGamer]) and (rmngEGP!=0)): # Если егп покупается меньше, чем продает игроком
            player.qplayers[numbersmix[ActualGamer]]['money']-=value[ActualGamer]*rmngEGP
            player.qplayers[numbersmix[ActualGamer]]['egp']-= rmngEGP
            print('Прибыль игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' = ',value[ActualGamer]*rmngEGP)
            rmngEGP=0
        else: # если было скупленнно нужное кол-во егп
            print('   Заказчик закупил максимальное кол-во ЕГП ')
        print('Деньги игрока ',player.qplayers[numbersmix[ActualGamer]]['name'],' c учетом прибыли = ',player.qplayers[numbersmix[ActualGamer]]['money'])