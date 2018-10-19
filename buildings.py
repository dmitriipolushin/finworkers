import player
def buildings():
    for i in range(player.curNumOfGamers):
        print('Вы хотите строить фабрики в этом месяце?[y/n]')
        ans = input()
        if ans == 'y':
            continue
        else:
            return
        print('Вы хотите построить обычные фабрики?[y/n]')
        ans = input()
        if ans == 'y':
            print('Сколько обычных фабрик вы хотите построить?(Каждая фабрика стоит 5000дол)')
            qua = int(input())
            while player.players[i]['money'] < qua*5000):
                qua = int(input('Error: У вас недостаточно средств.\n \nКаждая обычная фабрика стоит 5000дол.\nВведите другое число'))
            player.players[i]['money'] -= qua*5000
            print('оставшиеся деньги:', player.players[i]['money'])
            for j in range(qua) 
            player.players[i][buildings[j]]['bfactory'] += qua 
            player.players[i][buildings[j]]['DLf'] = 5
            