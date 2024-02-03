# открываем файл на чтение с кодировкой ютф 8
with open('space.txt', 'r', encoding='utf-8') as file:
    data = file.readlines() # считываем строки
    machines = [] # список со всеми данными
    # цикл для разделения информации из одной строки в список
    for i in data[1:]:
        machines.append(i.strip().split('*'))
numbers_name = []
numbers_num = []
# перебираем информацию
for machine in machines:
    number_ship = int(machine[0][5:8]) # номер коробля
    numbers_name.append([number_ship, machine[0]]) # заносим в список
    numbers_num.append(number_ship)
count = 0
i = 0
# сортировка пока не будет 10 кораблей
while count < 10:
    i += 1 # перебираем номера корабля пок ане встретяться 10 самых наименьших
    if i in numbers_num:
        count += 1
        # берем корабль из списка под данным номером и выводим
        for elem in numbers_name:
            if elem[0] == i:
                print(elem[0],elem[1])
                break
