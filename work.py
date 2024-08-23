import re
import json
with open('My_file.txt', 'r', encoding='utf-8') as fl:
    source_list = fl.readlines()

company_profit_dict = {}
total_profit = 0
count_profit = 0
for line in source_list:
    values = re.findall(r'\d+', line) 
    values = list(map(int, values))
    profit = values[0] - values[1]
    total_profit += profit if profit >= 0 else 0
    count_profit += 1 if profit >= 0 else 0
    company_name = line.split(' ')[0].strip()   
    company_profit_dict[company_name] = profit 

average_profit_dict = {'average_profit': round(total_profit / count_profit)}
result_list = [company_profit_dict, average_profit_dict]

# Сохраняем данные в файл 'data.json'
with open('My_file_5.7.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)
    print(f)