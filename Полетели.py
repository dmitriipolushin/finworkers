building = {'view': 0,'DL': 0} # Создаем единую для всех видов строительства запиську билдинг
loan = {'qnt', 'DL'}# Это записька ссуды: qnt - сумма ссуды, DL - дата выплаты(Дедлайн)
buildings = []
for i in range(6):
    buildings.append(building) # В итоге имеем массив из 6 записек билдингов(макс. кол-во фабрик)
playerLoans = []
for i in range (6):
    playerLoans.append(loan) # ссуды берутся под фабрики, поэтому их тоже 6
"""
 В принципе сейчас мы можем так и не делать, а добавлять новую ссуду или стройку в массив по ходу его появления
"""

# Непосредственно записька игрока

player = {'money': 10000,      # Денежки
          'factory': 2,        # Кол-во обыч. Фабрик
          'autoFactory': 0,    # Кол-во автомат.Фабрик
          'esm': 4,            # Кол-во ЕСМ
          'egp': 2,            # Кол-во ЕГП
          'buildings': buildings,# Все происходящие в данный момент строительства
          'loans': playerLoans,  # Массив с ссудами игрока
         }
Players = []
for i in range(12):
    Players.append(player)
print(Players[0]['buildings'][0]['view'])

