# открываем файл на чтение с кодировкой ютф 8
with open('space.txt', 'r', encoding='utf-8') as file:
    data = file.readlines() # считываем строки
    machines = [] # список со всеми данными
    # цикл для разделения информации из одной строки в список
    for i in data[1:]:
        machines.append(i.strip().split('*'))
write_list = []
# основной цикл
for machin in machines:
    n,m = machin[0][5:7] #берем из информации n и m
    t = len(machin[1]) # считаем количество букв в названии планеты
    x_d, y_d = machin[3].split(' ') # считываем координты вектора
    n, m = int(n), int(m)
    x_d, y_d = int(x_d), int(y_d)
    # ВЫШЕ ИНТУЕМ ЧТОБЫ ИЗ СТРОКИ СДЕЛАТЬ ЧИСЛО

    #Расчет по форумлам из задачи
    if n > 5:
        x = n + x_d
    else:
        x = -(n + x_d) * 4 + t
    if m > 3:
        y = m + t + y_d
    else:
        y = -(n + y_d) * m

    # Заносим в список для записи нужные планеты и их новые координаты
    if machin[0][3] == 'V':
        write_list.append(f'{machin[0]}-({x}, {y})\n')

    # Открывем файл на запись и записываем туда наш список с планетами по строкам
    with open('space_new.txt', 'w', encoding='UTF-8') as file_w:
        file_w.writelines(write_list)
