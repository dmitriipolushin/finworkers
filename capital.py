'''
Функция переподсчета капитала игроков.
Должна вызываться перед процедурой ссуд и процедурой проигравших

'''
import player
import math as m
def capitalFunc(Lvl):
    for ActualGamer in range(player.CurNumOfGamers):
        a=[[player.CurNumOfGamers,800,3*player.CurNumOfGamers,6500],
        [m.trunc(1.5*player.CurNumOfGamers),650,m.trunc(2.5*player.CurNumOfGamers),6000],
        [2*player.CurNumOfGamers,500,2*player.CurNumOfGamers,5500],
        [m.trunc(2.5*player.CurNumOfGamers),400,m.trunc(1.5*player.CurNumOfGamers),5000],
        [3*player.CurNumOfGamers,300,player.CurNumOfGamers,4500]]
        player.qplayers[ActualGamer]['capital'] = (
            player.qplayers[ActualGamer]['factory']*5000 + 
            player.qplayers[ActualGamer]['autoFactory']*7000 + player.qplayers[ActualGamer]['esm']*a[Lvl-1][1] + 
            player.qplayers[ActualGamer]['egp']*a[Lvl-1][3] + player.qplayers[ActualGamer]['money']
        )
    return