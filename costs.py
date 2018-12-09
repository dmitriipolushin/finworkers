import player
def monthlyCosts():
    allCosts = 0
    for i in range(player.CurNumOfGamers):
        #print(player.qplayers)
        #print('dengi',player.qplayers[i]['money'],'igroka',i+1)
        allCosts = (player.qplayers[i]['esm']*300 + player.qplayers[i]['egp']*500 + 
            player.qplayers[i]['factory']*1000 + player.qplayers[i]['autoFactory']*1500)
        player.qplayers[i]['money'] -= allCosts
        allCosts = 0
    return