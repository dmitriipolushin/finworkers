import player

def winner():
    w = ''
    for i in player.qplayers:
        if i['money'] > w:
            w = i['name']