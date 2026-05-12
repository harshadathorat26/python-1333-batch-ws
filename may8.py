#task 1:Accept student information name,marks,per
#rahul scored 450 marks with 90.0%

# name = input("Enter student name:")
# marks = eval(input("Enter marks scored:"))
# percentage = eval(input("Enter percentage:"))
# s = f"{name} scored {marks} marks with {percentage:.1f}%"
# print(s)

#task 2:Accept age from user and display age after 10 years to user
# age = int(input("Enter your current age:"))
# print(f"your age will be {age+10} after 10 years.")

#task 3:Name Marks table
 
# name1 = "Amit"
# name2 = "Rohit"
# name3 = "Priya"
# marks1 = 78
# marks2 = 89
# marks3 = 92
# print("-" * 14)
# print(f"|{'Name':^6}|{'Marks':^7}|")
# print("-" * 14)
# print(f"|{name1:^6}|{marks1:^7}|")
# print("-" * 14)
# print(f"|{name2:^6}|{marks2:^7}|")
# print("-" * 14)
# print(f"|{name3:^6}|{marks3:^7}|")
# print("-" * 14)

#task4 : generate a report card 
#title - the kiran acadamy report card 
# student name : harshada thorat
# subject name-python ,java,html,css,sql
# marks-91,90,88,95,96
# total-470
# Grade - A
name = input("Enter your name:")
sub1 = "Python"
sub2 = "Java"
sub3 = "Html"
sub4 = "Css"
sub5 = "Sql"
marks1 = 91
marks2 = 90 
marks3 = 88
marks4 = 95
marks5 = 96
total = 470
grade = "A"

print(f"{'='*5} {'The Kiran Academy Report Card'} {'='*5}")
print(f"{'='*3} {'Student Name:'}{name} {'='*3}")
print (f"|{'Subject':^10}|{'Marks':^7}|")
print (f"|{sub1:^10}|{marks1:^7}|")
print (f"|{sub2:^10}|{marks2:^7}|")
print (f"|{sub3:^10}|{marks3:^7}|")
print (f"|{sub4:^10}|{marks4:^7}|")
print (f"|{sub5:^10}|{marks5:^7}|")
print(f"{'='*24}")
print(f"|{'Total':^10}|{total:^7}|")
print(f"{'='*24}")
print(f"|{'Grade':^10}|{grade:^7}|")