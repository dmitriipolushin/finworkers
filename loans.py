'''
Процедура взятия ссуд

Для ссуд есть два варианта реализации.
В связи с отличным от Pascal устройством оператора присваивания, здесь ссуды каждого игрока будут ссылаться на один и
тот же массив, если полностью перевести аналогичную процедуру с паскалевской версии.

1-ый вариант:
    Для каждого игрока завести массив Loans, состоящий изначально из 6-ти элементов (макс.кол-во ссуд) и завести 
    переменную LoansQnt, обозначающую кол-во ссуд у игрока и сколько элементов массива Loans будут заполнены.
    Такой вариант как раз был в паскале в первоначальной версии, но здесь может работать неправильно. 
2-ой вариант:
    Массив Loans игрока изначально делать пустым, и добавлять в него новый элемент (равный словарю Loan) при получении ссуды.
    В Python такой вариант наиболее удобен в реализации(можно обращаться к последнему элементу через -1 вместо переменной 
    LoansQnt), и не должно происходить ошибок с присваиванием.
    
Сейчас реализован второй вариант.
'''

import player
def LoansFunc(Lvl,mes):
    for ActualGamer in range(player.CurNumOfGamers):
        answer1 = 1
        answer2 = 1
        while (answer1 == 1):
            if (player.qplayers[ActualGamer]['FreeAutoFac']==0) and (player.qplayers[ActualGamer]['FreeFac']==0):
                print("Игрок ",player.qplayers[ActualGamer]['name']," не может получить ссуду, т.к. у него нет свободных фабрик.")
                break
            if (player.qplayers[ActualGamer]['LoansSum']+5000>player.qplayers[ActualGamer]['capital']//2):
                if (player.qplayers[ActualGamer]['LoansSum']+10000>player.qplayers[ActualGamer]['capital']//2):
                    print(
                        "Игрок ",player.qplayers[ActualGamer]['name'],
                        " не может взять ссуду, т.к. при ее получении он превысит половину гарантированного капитала"
                        )
                break
            print("Хотите ли получить ссуду?")
            print("Введите 1, если да, и любой другой символ, если нет.")
            answer1 = int(input())
            if answer1 == 1:
                if (player.qplayers[ActualGamer]['FreeAutoFac']==0) and(player.qplayers[ActualGamer]['FreeFac']==0):
                    print("Игрок ",player.qplayers[ActualGamer]['name']," не может получить ссуду, т.к. у него нет свободных фабрик.")
                    break
                if (player.qplayers[ActualGamer]['LoansSum']+5000>player.qplayers[ActualGamer]['capital']//2):
                    print(
                        "Игрок ",player.qplayers[ActualGamer]['name'],
                        " не может взять ссуду, т.к. при ее получении он превысит половину гарантированного капитала"
                        )
                    break
                print("Под какую фабрику?")
                print("Под обычную фабрику выдается 5000 долл., под автоматизированную 10000 долл. ")
                if (player.qplayers[ActualGamer]['FreeAutoFac']!= 0) and (player.qplayers[ActualGamer]['FreeFac']!=0):
                    print("У вас есть свободные обычные и автоматизированные фабрики")
                elif (player.qplayers[ActualGamer]['FreeFac']!=0):
                        print("У вас есть только обычные свободные фабрики")
                else:
                    print("У вас есть только автоматизированные свободные фабрики")
                while (answer2!=1) and (answer2!= 2) and (answer2!=0):
                    print("Введите: 1 - под обычную, 2 - автоматизированную, 0 - отмена")
                    answer2 = input()
                if answer2 == 1:
                    player.qplayers[ActualGamer]['FreeFac']-= 1
                elif answer2 == 2:
                    player.qplayers[ActualGamer]['FreeAutoFac']-=1
                loan = {'qnt':0, 'DL':0} #Словарь Loan по-умолчанию
                player.qplayers[ActualGamer]['loans'].append(loan)
                player.qplayers[ActualGamer]['loans'][-1]['qnt']= answer2 * 5000
                player.qplayers[ActualGamer]['loans'][-1]['DL']= mes +12
                player.qplayers[ActualGamer]['money']+= answer2 * 5000
                player.qplayers[ActualGamer]['LoansSum']+= answer2 * 5000
                print("Игрок ",player.qplayers[ActualGamer]['name']," получил ссуду суммой ", answer2*5000)
    return
'''
Процедура выплаты ссудного процента

'''
def LoansPercents():
    for ActualGamer in range(player.CurNumOfGamers): # Хрен пойми когда, кем и зачем, но было введено поле LoansSum, которое здесь удачно применяется
        player.qplayers[ActualGamer]['money']-player.qplayers[ActualGamer]['LoansSum']*0.01
    return
'''
Процедура погашения ссуд

'''
def LoansRepayment(mes):
    for ActualGamer in range(player.CurNumOfGamers):
        for ActualLoan in range(len(player.qplayers[ActualGamer]['loans'])):
            if player.qplayers[ActualGamer]['loans'][ActualLoan]['DL'] == mes:
                player.qplayers[ActualGamer]['money']-=player.qplayers[ActualGamer]['loans'][ActualGamer]['qnt']
    return