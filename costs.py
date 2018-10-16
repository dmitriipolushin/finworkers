import player
player.player['money'] -= (player.player['esm']*300 + player.player['egp']*500 + 
    player.player['factory']*1000 + player.player['autoFactory']*1500)
print(player.player['money'])
