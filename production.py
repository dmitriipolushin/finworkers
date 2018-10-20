import player
def productionEgp():
    for i in range(player.curNumOfGamers):
        ans = input('Вы хотите производить продукцию в этом месяце?[y/n]:')
        if ans == 'y':
            qua = int(input('Сколько ЕСМ вы хотите переработать?'))
            while qua > player.players[i]['esm']:
                qua = input('У вас недостаточно ЕСМ, введите другое число')
            quaCommon = int(input('Сколько ЕСМ вы хотите переработать на обычных фабриках?'))
            while quaCommon > player.players[i]['factory']:
                quaCommon = int(input('У вас недостаточно обычных фабрик, введите другое число'))
            player.players[i]['esm'] -= quaCommon
            player.players[i]['egp'] += quaCommon
            player.players[i]['money'] -= quaCommon*2000
            quaAuto = int(input('Сколько ЕСМ вы хотите переработать на автоматических фабриках?'))
            while quaAuto > player.players[i]['autoFactory']*2:
                quaAuto = int(input('У вас недостаточно обычных фабрик, введите другое число'))
            player.players[i]['esm'] -= quaAuto
            player.players[i]['egp'] += quaAuto
            player.players[i]['money'] -= quaAuto*1500