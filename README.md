# finworkers
  В эту дирректорию будут загружаться все механики, необходимые для того, чтобы сыграть в игру "Финансовые воротилы". Здесь находтся описание взаимодействий механик в ходе игры.
  Вначале игры у каждого игрока появляется начальный капитал. Также нам нужно постоянно изменять данные игрока и хранить их. Поэтому у нас есть механика, в которой создается база данных с информацией для каждого игрока(player.py). Для каждого игрока создаётся словарь с записями. Для каждого игрока хранится информация о колличестве его денег('money'), обычных фабрик('factory'), автоматических фабрик('autoFactory'), ЕСМ и ЕГП('esm', 'egp'), строительств('buildings'). В записи строительств содержится информация о том, сколько у игрока сторится обычных фабрик('bfactory'), автоматизированных фабрик('bAFactory') и через сколько построится та или иная фабрика('DLf' - для обычной фабрики, 'DLaf' - для автоматизированной фабрики), а также через сколько автоматизируется обычная фабрика('upgrade'), если есть фабрики, которые автоматизируются. Также здесь содержится список ссуды('loans'), в котором  информация о том, сколько у игрока ссуд('qnt'), и когда ему необходимо их выплатить('DL'). 
  
  Начальная ситуация. У каждого игрока в начале игры есть определенное количество ресурсов. Оно одинаковое для всех игроков. Каждый игрок (президент компании) получает две обычные фабрики, четыре единицы сырья и материалов (сокращенно ЕСМ), две единицы готовой продукции (сокращенно ЕГП) и 10000 долл. наличными. Игроки занумерованы от 1 до N, и в первом круге игрок 1 — старший. С каждым кругом (т. е. ежемесячно) роль старшего переходит к следующему по порядку номеров игроку, после N-го старшим становится опять первы
  
  Теперь приступим к описанию игрового процесса.
  
  В игровой цикл входит 
1. Постоянные издержки. 
2. Определение обстановки на рынке.
3. Заявки на сырье и материалы. 
4. Производство продукции.
5. Продажа продукции.
6. Выплата ссудного процента.
7. Погашение ссуд.
8. Получение ссуд.
9. Заявки на строительство
Все пункты цикла выполняются последовательно.

Для всех пунктов игрового цикла у нас предусмотренны 11 механик. Про первую механику мы рассказывали в самом начале.
Механики игры:
1) База данных с данными игроков
2) Постоянные издержки
3) Обстановка на рынке(сюда же входит переход по уровням, и сюда же входит определение старшего игрока)
4) Заявки на ЕСМ
5) Производство(учитывая фабрики)
6)Продажа ЕГП
7) Выплата ссудного процента
8) погашение ссуд
9) Получение ссуд
10) Заявки на строительство
11) Результаты игры
