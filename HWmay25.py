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


       

