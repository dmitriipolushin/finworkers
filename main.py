import player
import costs
print('Добро пожаловать в игру финансовые воротилы!')
print('\n Сколько будет игрроков?')
curNumOfGamers = int(input())
players = []
for i in range(curNumOfGamers):
    players.append(player.player)
for i in range(len(players)):
    costs.monthlyCosts(players[i])
print(players[0]['money']) 
