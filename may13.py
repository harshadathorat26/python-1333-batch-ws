#Net salary (Total) calaulation of Employees
#Accept name and Basic salary amount of an employee
#HRA=10%,DA=20% ,PF=12%

name = input("Enter name of employee:")
basic_salary = float(input("Enter your basic salary:"))
print("")
print("")
print(f"{('-')*24}")
print("SALARY SLIP")
print(f"{('-')*24}")
print(f"{'Name':^12} = {name:^12}")
print(f"{'Basic_salary':^12} = {basic_salary:^12}")
print(f"{'HRA':^12} = {basic_salary*(10/100):^12}")
print(f"{'DA':^12} = {basic_salary*(20/100):^12}")
print(f"{'PF':^12} = {basic_salary*(12/100):^12}")
print(f"{('-')*24}")
net_salary = basic_salary + basic_salary*(10/100) + basic_salary*(20/100) -basic_salary*(12/100)
print(f"{'Net Salary':^12} = {net_salary:^12}")
print(f"{('-')*24}")
