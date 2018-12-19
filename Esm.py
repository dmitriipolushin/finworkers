import player
import mix
import tabl
import math as m
import os
def AcquisitionOfEsm (Lvl):
    a=[[player.CurNumOfGamers,800,3*player.CurNumOfGamers,6500],
    [m.trunc(1.5*player.CurNumOfGamers),650,m.trunc(2.5*player.CurNumOfGamers),6000],
    [2*player.CurNumOfGamers,500,2*player.CurNumOfGamers,5500],
    [m.trunc(2.5*player.CurNumOfGamers),400,m.trunc(1.5*player.CurNumOfGamers),5000],
    [3*player.CurNumOfGamers,300,player.CurNumOfGamers,4500]]
    prESM,qntESM = 0,0 # прцедура для приобретения есм игроками 
    for ActualGamer in range(player.CurNumOfGamers):
        print('Обстановка на рынке:')
        print('Общее кол-во продаваемых ЕСМ= ',a[Lvl-1][0],', МинЦенаЕСМ= ',a[Lvl-1][1])
        print('Игрок ',ActualGamer+ 1)
        print('Ваши деньги = ',player.qplayers[ActualGamer]['money'])
        print('Сколько ЕСМ вы хотите приобрести? ')
        qntESM=int(input())
        while (qntESM>a[Lvl-1][0]):
            print('Недопустимое кол-во. Вы можете приобрести менее ',a[Lvl-1][0],' ЕСМ ')
            print('Введите другое кол-во ')
            qntESM=int(input())
        if (qntESM != 0):
            print('По какой цене? ')
            prESM=int(input())
            while((player.qplayers[ActualGamer]['money'] - prESM*qntESM)<0) or (prESM<a[Lvl-1][1]) or (qntESM>a[Lvl-1][0]): #Здесь он проверяет все ли в порядке с заявкой
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
        os.system('cls')
    mix.mixEsmEgp()
    mix.satisfactionEsm(tabl.Level, a[tabl.Level][0])
    return