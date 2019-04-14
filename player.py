CurNumOfGamers=0
qplayers = []
def players():
    buildings = []
    for i in range(6):
        building = {'bfactory': 0,'DLf': 0, 'bAFactory': 0, 'DLaf': 0, 'upgrade': 0} # Создаем единую для всех видов строительства запиську билдинг
        buildings.append(building) # В итоге имеем массив из 6 записек билдингов(макс. кол-во фабрик, которое можно построить)
    playerLoans = []
    for i in range (6):
        loan = {'qnt', 'DL'}# Это записька ссуды: qnt - сумма ссуды, DL - дата выплаты(Дедлайн)
        playerLoans.append(loan) # ссуды берутся под фабрики, поэтому их тоже 6
    # Непосредственно записька игрока
    print('\n Сколько будет игроков?')
    global CurNumOfGamers
    CurNumOfGamers = int(input())
    for i in range(CurNumOfGamers):
        player = {'name': input('Введите свое имя '),
            'money': 10000,      # Денежки
            'factory': 2,        # Кол-во обыч. Фабрик
            'autoFactory': 0,    # Кол-во автомат.Фабрик
            'esm': 4,            # Кол-во ЕСМ
            'egp': 2,            # Кол-во ЕГП
            'buildings': buildings,# Все происходящие в данный момент строительства
            'loans': playerLoans}  # Массив с ссудами игрока
        qplayers.append(player)
    return