#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
#Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
#Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, output_in_hours, rate_per_hour, bonus = argv 

def payroll_calculation(output_in_hours, rate_per_hour, bonus):
    # Преобразуем строки в числа
    output_in_hours = float(output_in_hours)
    rate_per_hour = float(rate_per_hour)
    bonus = float(bonus)
    payroll = (output_in_hours * rate_per_hour) + bonus
    return payroll

print(payroll_calculation(output_in_hours, rate_per_hour, bonus))