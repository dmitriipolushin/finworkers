CurNumOfGamers=0
qplayers = []
def players():
    buildings = []
    for i in range(6):
        building = {'bfactory': 0,'DLf': 0, 'bAFactory': 0, 'DLaf': 0, 'upgrade': 0} # Создаем единую для всех видов строительства запиську билдинг
        buildings.append(building) # В итоге имеем массив из 6 записек билдингов(макс. кол-во фабрик, которое можно построить)
    playerLoans = []
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
            'loans': playerLoans, # Массив с ссудами игрока
            'LoansSum': 0, # сумма непогашенных ссуд
            'capital':33000,  # Гарантированный капитал 
            'FreeFac':2,   # Кол-во фабрик доступных для взятия под них ссуд 
            'FreeAutoFac':0} # Кол-во автоматизированных фабрик доступных для взятия под них ссуд 
        qplayers.append(player)
    return