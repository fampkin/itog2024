import csv
# открываем файл на чтение с кодировкой ютф 8
with open('space.txt', 'r', encoding='utf-8') as file:
    data = file.readlines() # считываем строки
    machines = [] # список со всеми данными
    # цикл для разделения информации из одной строки в список
    for i in data[1:]:
        machines.append(i.strip().split('*'))
# перебираем информацию
for machine in machines:
    ind = machines.index(machine)
    name_planet_last_3_letters = machine[1][-3:].upper()
    letters_from_code = machine[0][2].upper() + machine[0][1].upper()
    name_planet_first_3_letters_reversed = machine[1][:3].upper()
    password = name_planet_last_3_letters + letters_from_code + name_planet_first_3_letters_reversed
    machines[ind] = f'{machine[0]};{machine[1]};{machine[2]};{machine[3]};{password}'
print(machines)
with open('space_uniq_password.csv', 'w', encoding='utf-16') as file:
    csv_writer = csv.writer(file)
    for i in machines:
        csv_writer.writerow([i[0], i[1]])
