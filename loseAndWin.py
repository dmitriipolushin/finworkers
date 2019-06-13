import player

def loser():
    check = 0
    for pl in player.qplayers:
        if pl['money'] <=  0 and pl['esm'] * 650 < abs(pl['money']):
            print('Игрок ', pl['name'], 'выбывает, так как он обанкротился и не имеет возможности выйти в плюс')
            player.qplayers.remove(pl-check)
            check += 1
def winner():
    for pl in player.qplayers:
        pl['AllSavings'] = pl['esm'] * 800 + pl['egp'] * 6500 + pl['money']
    check = player.qplayers[0]['AllSavings']
    check1 = player.qplayers[0]['name']
    for pl in player.qplayers:
        if pl['AllSavings'] > check:
            check1 = pl['name'] 
            check = pl['AllSavings']
    print(check1, '- ты выиграл в игре Финансовые воротилы! Поздравляю!')