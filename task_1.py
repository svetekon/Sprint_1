time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разбиваем строку по запятым 
time_blocks = time_string.split(',')

total_minutes = 0

for block in time_blocks:
    # Разбиваем блок по пробелам, чтобы получить отдельные значения вроде '1h', '45m'
    parts = block.split()
    
    for part in parts:
        if 'h' in part:
            # Переводим часы в минуты
            hours = int(part.replace('h', ''))
            total_minutes += hours * 60
            
        elif 'm' in part:
            # Прибавляем минуты к часам
            minutes = int(part.replace('m', ''))
            total_minutes += minutes
            
        elif 's' in part:
            # Прибавляем секунды 
            seconds = int(part.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes) 