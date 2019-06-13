import player
def buildings(i):
    print('Игрок ',player.qplayers[i]['name'])
    print('У вас ',player.qplayers[i]['factory'],' Обычных фабрик')
    print('У вас ',player.qplayers[i]['autoFactory'],' автоматизированных фабрик')
    print('Вы хотите строить фабрики в этом месяце?[y/n]')
    #print('У вас ',sum(player.qplayers[i]['buildings'][]['bfactory']),'строящихся обычных фабрик')
    ans = input()
    if ans != 'y':
        return
    print('Вы хотите построить обычные фабрики?[y/n]')
    ans = input()
    if ans == 'y':
        print('Сколько обычных фабрик вы хотите построить?(Каждая фабрика стоит 5000дол)')
        qua = int(input())
        while (player.qplayers[i]['money'] < qua*5000):
            qua = int(input('Error: У вас недостаточно средств.\n \nКаждая обычная фабрика стоит 5000дол.\nВведите другое число'))
        player.qplayers[i]['money'] -= qua*5000
        print('оставшиеся деньги:', player.qplayers[i]['money'])
        for j in range(qua): 
            player.qplayers[i]['buildings'][j]['bfactory'] += 1 
            player.qplayers[i]['buildings'][j]['DLf'] = 5        
        for k in range(6):
            if player.qplayers[i]['buildings'][k]['bfactory'] != 0:
                player.qplayers[i]['buildings'][k]['DLf'] -= 1
                if player.qplayers[i]['buildings'][k]['DLf'] == 0:
                    player.qplayers[i]['factory'] += 1
    print('Вы хотите построить автоматические фабрики?[y/n]')
    ans = input()
    if ans == 'y':
        print('Сколько автоматизированных фабрик вы хотите построить?(Каждая фабрика стоит 10000дол)')
        qua = int(input())
        while (player.qplayers[i]['money'] < qua*10000):
            qua = int(input('Error: У вас недостаточно средств.\n \nКаждая обычная фабрика стоит 10000дол.\nВведите другое число'))
        player.qplayers[i]['money'] -= qua*10000
        print('оставшиеся деньги:', player.qplayers[i]['money'])
        for j in range(qua): 
            player.qplayers[i]['buildings'][j]['bAFactory'] += 1
            player.qplayers[i]['buildings'][j]['DLaf'] = 7
        for k in range(6):
            if player.qplayers[i]['buildings'][k]['bAFactory'] != 0:
                player.qplayers[i]['buildings'][k]['DLaf'] -= 1
                if player.qplayers[i]['buildings'][k]['DLaf'] == 0:
                    player.qplayers[i]['autoFactory'] += 1
    print('Вы хотите улучшить обычные фабрики до автоматических?[y/n]')
    ans = input()
    if ans == 'y':
        print('Сколько обычных фабрик вы хотите улучшить?(Каждая фабрика стоит 7000дол)')
        qua = int(input())
        while (player.qplayers[i]['money'] < qua*7000):
            qua = int(input('Error: У вас недостаточно средств.\n \nКаждая обычная фабрика стоит 7000дол.\nВведите другое число'))
        player.qplayers[i]['money'] -= qua*7000
        print('оставшиеся деньги:', player.qplayers[i]['money'])
        for j in range(qua):
            player.qplayers[i]['buildings'][j]['upgrade'] = 9
        for k in range(6):
            if player.qplayers[i]['buildings'][k]['upgrade']!=0:
                player.qplayers[i]['buildings'][k]['upgrade'] -= 1
                if player.qplayers[i]['buildings'][k]['upgrade'] == 0:
                    player.qplayers[i]['factory'] -= 1
                    player.qplayers[i]['autoFactory'] += 1