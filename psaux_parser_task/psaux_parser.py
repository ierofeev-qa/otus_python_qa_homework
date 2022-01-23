import re

from subprocess import run, PIPE
from collections import defaultdict
from datetime import datetime

currect_time = datetime.now()
result_filename = '{}-scan'.format(currect_time.strftime("%d-%m-%Y-%H:%M"))
user_list = []
process_counter = 0
processes_by_user = defaultdict(int)
processes_by_cpu = defaultdict(float)
processes_by_memory = defaultdict(float)
processes_by_user_formatted = ''
total_cpu_usage = 0
total_memory_usage = 0

process_info = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)
process_info_output = process_info.stdout.decode('utf-8')

with open(f'{result_filename}.txt', "x", encoding='UTF-8') as f:
    f.write(process_info_output)

with open(f'{result_filename}.txt', "r", encoding='UTF-8') as f:
    next(f)
    for line in f:
        pattern = re.search(r"(.*?)\s+(\S.*?)\s+(\S.*?)\s+(\S.*?)\s+(\S.*?)"
                            r"\s+(\S.*?)\s+(\S.*?)\s+(\S.*?)\s+(\S.*?)\s+(\S.*?)\s+(\S.*)", line)
        if pattern:
            user = pattern.group(1)
            cpu_usage = pattern.group(3)
            memory_usage = pattern.group(4)
            process = pattern.group(11)

            process_counter += 1
            user_list.append(user)
            processes_by_user[user] += 1
            total_cpu_usage += float(cpu_usage.replace(',', '.'))
            total_memory_usage += float(memory_usage.replace(',', '.'))
            processes_by_cpu[process] = cpu_usage
            processes_by_memory[process] = memory_usage

processes_by_user = sorted(processes_by_user.items(), key=lambda kv: kv[1], reverse=True)
for i in processes_by_user:
    processes_by_user_formatted += '\n{}: {}'.format(i[0], i[1])

processes_by_cpu = sorted(processes_by_cpu.items(), key=lambda kv: float(kv[1]), reverse=True)
processes_by_memory = sorted(processes_by_memory.items(), key=lambda kv: float(kv[1]), reverse=True)

system_scan = f"Отчёт о состоянии системы:\n"\
              f"Пользователи системы: {', '.join(x for x in set(user_list))}\n"\
              f"Процессов запущено: {process_counter}\n"\
              f"Пользовательских процессов: {processes_by_user_formatted}\n"\
              f"Всего памяти используется: {round(total_memory_usage, 2)}%\n"\
              f"Всего CPU используется: {round(total_cpu_usage, 2)}%\n"\
              f"Больше всего памяти использует: {processes_by_memory[0][0][:20]}\n"\
              f"Больше всего CPU использует: {processes_by_cpu[0][0][:20]}\n"

with open(f'{result_filename}.txt', "w", encoding='UTF-8') as f:
    f.write(system_scan)

print(system_scan)
