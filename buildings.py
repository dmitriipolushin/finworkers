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
            print('Сколько обычных фабрик вы хотите построить?')
            qua = int(input())
            while player.players[i]['money'] < qua*5000):
                qua = int(input('Error: У вас недостаточно средств. Введите другое число'))
            

            