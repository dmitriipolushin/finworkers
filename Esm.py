import numpy as np
import player
value = np.zeros((10))
quantity = np.zeros_like(value)
numbersmixESM = np.zeros_like(value)
def AcquisitionOfEsm (Lvl):
    prESM,qntESM = 0,0 # прцедура для приобретения есм игроками
    for ActualGamer in range(CurNumOfGamers):
        print('Обстановка на рынке:')
        print('Общее кол-во продаваемых ЕСМ= ',a[Lvl-1][0],', МинЦенаЕСМ= ',a[Lvl-1][1])
        print('Игрок ',ActualGamer+ 1)
        print('Ваши деньги = ',player.players[ActualGamer]['money'])
        print('Сколько ЕСМ вы хотите приобрести? ')
        qntESM=int(input())
        while (qntESM>a[Lvl-1][0]):
            print('Недопустимое кол-во. Вы можете приобрести менее ',a[Lvl-1][0],' ЕСМ ')
            print('Введите другое кол-во ')
            qntESM=int(input())
        if (qntESM != 0):
            print('По какой цене? ')
            prESM=int(input())
            while((player.players[ActualGamer]['money'] - prESM*qntESM)<0) or (prESM<a[Lvl-1][1]) or (qntESM>a[Lvl-1][0]): #Здесь он проверяет все ли в порядке с заявкой
                print('Недопустимая сумма')
                print('Введите другую цену или кол-во ЕСМ')
                print('Кол-во ')
                qntESM=int(input())
                print('Цена ')
                prESM=int(input())
        value[ActualGamer] = prESM
        quantity[ActualGamer]=qntESM
        numbersmixESM[ActualGamer] = ActualGamer
        print('Цена за одну ЕСМ в заявке игрока ',ActualGamer+1,' = ',value[ActualGamer])
        print('Общая сумма заявки= ',prESM*qntESM)
        return
def mixEsm():
    for ActualGamer in range(CurNumOfGamers-1):
        for i in range(CurNumOfGamers-ActualGamer):
            if value[d]<value[d+1]:
                z = value[d] #Сортировка цен
                value[d] = value[d+1]
                value[d+1] = z
                u = quantity[d] #Сортировка кол-ва
                quantity[d]= quantity[d+1]
                quantity[d+1]= u
                xx= numbersmixESM[d]
                numbersmixESM[d]= numbersmixESM[d+1]
                numbersmixESM[d+1]=xx
    for ActualGamer in range(CurNumOfGamers):
        if (quantity[ActualGamer]=0):
            print('Игрок ',ActualGamer,' не делал заявки ')
        else:
            print(ActualGamer,'. ','Заявка игрока ',numbersmixESM[ActualGamer],' величиной ',value[ActualGamer],' за одну ЕСМ')