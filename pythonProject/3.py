ShipName = input()
planet = ''
direction = ''
while ShipName != 'stop':
    # открываем файл на чтение с кодировкой ютф 8
    with open('space.txt', 'r', encoding='utf-8') as file:
        data = file.readlines() # считываем строки
        machines = [] # список со всеми данными
        # цикл для разделения информации из одной строки в список
        for i in data[1:]:
            machines.append(i.strip().split('*'))
    flag = False
    # перебираем информацию и если у нас есть корабль с таким именем с писке завпоминаем его родную планету и направление
    for machine in machines:
        if ShipName in machine:
            flag = True
            planet = machine[1]
            direction = machine[3]
    # проверяем встретлся ли такой корабль в списке и вовыдоим соот строку
    if flag:
        print(f'Корабль {ShipName} был отправлен с планеты: {planet}'
              f' и его направление движения было: {direction}')
    else:
        print('error.. er.. ror..')
    ShipName = input()