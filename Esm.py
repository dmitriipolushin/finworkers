import player
import mix
import tabl
def AcquisitionOfEsm (Lvl):
    prESM,qntESM = 0,0 # прцедура для приобретения есм игроками 
    for ActualGamer in range(player.CurNumOfGamers):
        print('Обстановка на рынке:')
        print('Общее кол-во продаваемых ЕСМ= ',tabl.a[Lvl-1][0],', МинЦенаЕСМ= ',tabl.a[Lvl-1][1])
        print('Игрок ',ActualGamer+ 1)
        print('Ваши деньги = ',player.qplayers[ActualGamer]['money'])
        print('Сколько ЕСМ вы хотите приобрести? ')
        qntESM=int(input())
        while (qntESM>tabl.a[Lvl-1][0]):
            print('Недопустимое кол-во. Вы можете приобрести менее ',tabl.a[Lvl-1][0],' ЕСМ ')
            print('Введите другое кол-во ')
            qntESM=int(input())
        if (qntESM != 0):
            print('По какой цене? ')
            prESM=int(input())
            while((player.qplayers[ActualGamer]['money'] - prESM*qntESM)<0) or (prESM<tabl.a[Lvl-1][1]) or (qntESM>tabl.a[Lvl-1][0]): #Здесь он проверяет все ли в порядке с заявкой
                print('Недопустимая сумма')
                print('Введите другую цену или кол-во ЕСМ')
                print('Кол-во ')
                qntESM=int(input())
                print('Цена ')
                prESM=int(input())
        mix.value[ActualGamer] = prESM
        mix.quantity[ActualGamer]=qntESM
        mix.numbersmix[ActualGamer] = ActualGamer
        print('Цена за одну ЕСМ в заявке игрока ',ActualGamer+1,' = ',mix.value[ActualGamer])
        print('Общая сумма заявки= ',prESM*qntESM)
    mix.mixEsmEgp()
    mix.satisfactionEsm(tabl.Level, tabl.a[tabl.Level][0])