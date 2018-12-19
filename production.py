import player
import os
def productionEgp():
    for i in range(player.CurNumOfGamers):
        print('Игрок ',i+1)
        print('У вас ',player.qplayers[i]['esm'],' ЕСМ.')
        ans = input('Вы хотите производить продукцию в этом месяце?[y/n]:')
        if ans == 'y':
            qua = int(input('Сколько ЕСМ вы хотите переработать?'))
            while qua > player.qplayers[i]['esm']:
                qua = input('У вас недостаточно ЕСМ, введите другое число')
            quaCommon = int(input('Сколько ЕСМ вы хотите переработать на обычных фабриках?'))
            while quaCommon > player.qplayers[i]['factory']:
                quaCommon = int(input('У вас недостаточно обычных фабрик, введите другое число'))
            player.qplayers[i]['esm'] -= quaCommon
            player.qplayers[i]['egp'] += quaCommon
            player.qplayers[i]['money'] -= quaCommon*2000
            quaAuto = int(input('Сколько ЕСМ вы хотите переработать на автоматических фабриках?'))
            while quaAuto > player.qplayers[i]['autoFactory']*2:
                quaAuto = int(input('У вас недостаточно обычных фабрик, введите другое число'))
            player.qplayers[i]['esm'] -= quaAuto
            player.qplayers[i]['egp'] += quaAuto
            player.qplayers[i]['money'] -= quaAuto*1500
        os.system('cls')
    return