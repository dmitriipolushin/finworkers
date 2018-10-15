bCommonFactory = {10}
bAutoFactory = {}
bUpgrade = {}
loan1 = {'qua': '10000', 'dL': '15'}
playerLoans = [loan1]
buildings = [bCommonFactory, bAutoFactory, bUpgrade]
dollars = 10000
player = {'money': dollars, 'factory': '1', 'autoFactory': '1', 'esm': '5',
         'egp': '5', 'buildings': buildings, 'loans': playerLoans}
print(player['buildings'][0])
