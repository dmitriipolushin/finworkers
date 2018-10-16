import player
def monthlyCosts(player):
    allCosts = (player.player['esm']*300 + player.player['egp']*500 + 
        player.player['factory']*1000 + player.player['autoFactory']*1500)
    player.player -= allCosts
    return allCosts
