def total_salary(path):
  total_sum = 0
  worker_count = 0
  try: 
    with open(path,"r" , encoding="utf-8") as file:
       for line in file:
        lines = line.strip().split(",")
        total_sum += int(lines[1])
        worker_count += 1
  except Exception as e:
        print(f"Помилка {e}")
        return None, None
  return total_sum , total_sum // worker_count

with open('salary_file.txt', 'w', encoding="utf-8") as salary:
    salary.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")