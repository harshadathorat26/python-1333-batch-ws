salary = [67000,45000,78000,55000,28000,44000,33000]

salary.sort()
print(salary)

second_max = salary[-2]
second_min = salary[+1]
print(f"second max is:{second_max}")
print(f"second min is:{second_min}")

# if salary.count(salary[-1]) == 1:
#     second_max = salary[-2]
# elif salary.count(salary[-1]) > 1:
#     second_max = salary[-1-salary.count(salary[-1])]
# print(second_max)


    