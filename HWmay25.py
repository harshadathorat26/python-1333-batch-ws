salary = [67000,45000,78000,55000,28000,44000,33000]

minimum = salary[0]
for i in range(len(salary)):
    if salary[i]< minimum:
        minimum = salary[i]
print(f"minimum salary among the above all is :{minimum}")

maximum = salary[0]
for i in range(len(salary)):
    if salary[i] > maximum:
        maximum = salary[i]
print(f"maximum salary among the above all is :{maximum}")

total = 0
for i in range(len(salary)):
    total += salary[i]
avg = total / len(salary)
print(f"Avg salary of employees is {avg}")

for i in range(len(salary)):
    if salary[i] < avg:
        if salary[i] == minimum:
            bonus = minimum * 10/100 + maximum * 5/100
            print(f"salary of minimum:{salary[i]} \t bonus:{bonus}")
        bonus = salary[i] * 10/100
        print(f"salary :{salary[i]} \t bonus:{bonus}")
        
    if salary[i] >=  avg:
        if salary[i] == maximum:
            print("no bonus for maximum salary!!")
        bonus = salary[i] * 5/100
        print(f"salary :{salary[i]} \t bonus:{bonus}")
       

