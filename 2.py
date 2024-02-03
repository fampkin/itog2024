# открываем файл на чтение с кодировкой ютф 8
with open('space.txt', 'r', encoding='utf-8') as file:
    data = file.readlines() # считываем строки
    machines = [] # список со всеми данными
    # цикл для разделения информации из одной строки в список
    for i in data[1:]:
        machines.append(i.strip().split('*'))
numbers_name = []
# перебираем информацию
for machine in machines:
    number_ship = int(machine[0][5:8]) # номер коробля
    numbers_name.append([number_ship, machine[0]]) # заносим в список
numbers_name.sort() # сортируем

# Выводим первые 10 кораблей
for elem in numbers_name[:10]:
    print(elem[1])
