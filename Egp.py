import player
import mix
import tabl
import math as m
def AcquisitionOfEgp(Lvl): #процедура для продажи егп игроками
    a=[[player.CurNumOfGamers,800,3*player.CurNumOfGamers,6500],
    [m.trunc(1.5*player.CurNumOfGamers),650,m.trunc(2.5*player.CurNumOfGamers),6000],
    [2*player.CurNumOfGamers,500,2*player.CurNumOfGamers,5500],
    [m.trunc(2.5*player.CurNumOfGamers),400,m.trunc(1.5*player.CurNumOfGamers),5000],
    [3*player.CurNumOfGamers,300,player.CurNumOfGamers,4500]]
    prEGP,qntEGP=0,0
    for ActualGamer in range(player.CurNumOfGamers):
        print('Обстановка на рынке:')
        print('Общее кол-во скупаемых ЕГП = ',a[Lvl-1][2],', МаксЦенаЕГП = ',a[Lvl][3])
        print('Игрок ',ActualGamer+1)
        print('Ваши деньги= ',player.qplayers[ActualGamer]['money'])
        print('Сколько ЕГП вы хотите продать? ')
        qntEGP=int(input())
        while(qntEGP>a[Lvl-1][2]):
            print('Недопустимое кол-во. Вы можете продать не более ',a[Lvl][2],' ЕГП ')
            print('Введите другое кол-во ')
            qntEGP=int(input())
        if (qntEGP!=0):
            print('По какой цене? ')
            prEGP=int(input())
            while (qntEGP>a[Lvl-1][2]) or (prEGP>a[Lvl-1][3]): #Здесь он проверяет все ли в порядке с заявкой
                print('Недопустимая сумма')
                print('Введите другую цену или кол-во ЕГП' )
                print('Кол-во ')
                qntEGP=int(input())
                print('Цена ');
                prEGP=int(input())
            value[ActualGamer]=prEGP
            quantity[ActualGamer]=qntEGP
            numbersmixESM[ActualGamer] = ActualGamer
            print('Цена за одну ЕГП в заявке игрока ',ActualGamer+1,' = ',value[ActualGamer])
            print('Общая сумма заявки= ',prEGP*qntEGP)
    mix.mixEsmEgp()
    mix.satisfactionEgp(tabl.Level, a[tabl.Level][2])