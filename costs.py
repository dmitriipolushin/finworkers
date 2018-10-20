import player
def monthlyCosts():
    for i in range(player.curNumOfGamers):
        allCosts = (player.players[i]['esm']*300 + player.players[i]['egp']*500 + 
            player.players[i]['factory']*1000 + player.players[i]['autoFactory']*1500)
        player.players[i]['money'] -= allCosts
    return 
