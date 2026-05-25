# l1 = [1,2,3]
# l2 = [5,6,7]
# print(l1 + l2)
# print(l1 - l2)
# print(l1 * 3.5)
# print(l1 / l2)
# print(l1 // l2)
# print(l1 % l2)

#Task1:find the total expenditure on employee salary
salary = [67000,45000,78000,55000,28000]
total = 0
for i in salary:
    total += i
print(f"Total expenditure on employee salary is :{total}")
#using range
i = len(salary)
tot=0
for i in range(0,5):
    tot += salary[i]
print(tot)
#using while
total_salary = 0
i = 4
while i >=0:
    total_salary += salary[i]
    i-=1
print(total_salary)

#using indexing
total1 = salary[0] +salary[1]+salary[2]+salary[3]+salary[4]
print(total1)
#using built in func
print(sum(salary))

#task2:salary of indivisuals at odd indices
total2 =0
for i in range(0,5):
    if i % 2 != 0:
        total2 += salary[i]
print(f"Salary of indivisuals at odd index :{total2}")

total3 = salary[1] + salary[3]
print(total3)

total4=0
for i in range(1,5,2):
    total4 += salary[i]


list2 = [salary[i] for i in range(5) if i % 2!=0]
print(sum(list2))

#sum at even indices
sum_even = 0
for i in range(0,5):
    if i % 2 == 0:
        sum_even += salary[i]
print(f"Sum of salaries at even insices:{sum_even}")

list3 = [salary[i] for i in range(5) if i % 2 ==0]
print(sum(list3))


#sum of first half
salary1 = [67000,45000,78000,55000,28000,44000,33000]
total_half = 0
length = len(salary1)//2
for i in range(0,length):
    total_half += salary1[i]
print(f"sum of first half is {total_half}")

#sum of other half
# total_half2 = 0
# for i in range(length,(len(salary1) + 1)):
#     total_half2 += salary1[i]
# print(f"sum of other half is {total_half2}")

print(sum(salary1) - total_half)

s = "Instagram"
l = len(s) // 2
print(s[0: l])

for i in range(len(s)//2):
    print(s[i])

# salary = [67000,45000,78000,55000,28000,44000,33000]

# minimum = salary[0]
# for i in range(len(salary)):
#     if salary[i]< minimum:
#         minimum = salary[i]
# print(f"minimum salary among the above all is :{minimum}")

# maximum = salary[0]
# for i in range(len(salary)):
#     if salary[i] > maximum:
#         maximum = salary[i]
# print(f"maximum salary among the above all is :{maximum}")

# total = 0
# for i in range(len(salary)):
#     total += salary[i]
# avg = total / len(salary)
# print(f"Avg salary of employees is {avg}")

# for i in range(len(salary)):
#     if salary[i] < avg:
#         if salary[i] == minimum:
#             bonus = minimum * 10/100 + maximum * 5/100
#             print(f"salary of minimum:{salary[i]} \t bonus:{bonus}")
#         bonus = salary[i] * 10/100
#         print(f"salary :{salary[i]} \t bonus:{bonus}")
        
#     if salary[i] >=  avg:
#         if salary[i] == maximum:
#             print("no bonus for maximum salary!!")
#         bonus = salary[i] * 5/100
#         print(f"salary :{salary[i]} \t bonus:{bonus}")
       

