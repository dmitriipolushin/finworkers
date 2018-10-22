import player
def monthlyCosts():
    for i in range(player.CurNumOfGamers):
        #print(player.qplayers)
        #print('dengi',player.qplayers[i]['money'],'igroka',i+1)
        allCosts = (player.qplayers[i]['esm']*300 + player.qplayers[i]['egp']*500 + 
            player.qplayers[i]['factory']*1000 + player.qplayers[i]['autoFactory']*1500)
        player.qplayers[i]['money'] -= allCosts
        #print('С игрока ',i+1,' списанно',allCosts)
        #print('dengi',player.qplayers[i]['money'],'igroka',i+1)
    return 