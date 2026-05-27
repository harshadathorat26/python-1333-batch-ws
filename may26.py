#Task1:find female and male count from census_data
# census_data = ['m','m','f','f','f','m','f','m','m','f','f','f','f']
# female_count = 0
# male_count = 0
# for gender in census_data:
#     if gender == 'm':
#         male_count +=1
#     else:
#         female_count +=1
# print(f"male count is :{male_count} and female count is :{female_count}")

#task2:find total count of students starting with P
# name = ['Ajay','Priya','Pavan','Viru','Raj','Payal','Rohan']
# count = 0
# for names in name:
#     if names.startswith('P'):
#         count +=1 
# print(f"Number of names starting with 'P' are :{count}")

# name_list = [x for x in name if x.startswith('P') == True]
# print(f"names starting with p are:{len(name_list)}")

# count1 = 0
# for names in name:
#     if 'P' in names[0]:
#         count1 +=1 
# print(f"Number of names starting with 'P' are :{count1}")

# count3 = 0
# for names in name:
#     if names[0] == 'P':
#         count3 +=1 
# print(f"Number of names starting with 'P' are :{count3}")

#Task 3:find total count of students whose name consists of two 'a'
# name = ['Ajay','Priya','Pavan','Viru','Raj','Payal','Rohan']
# count = 0
# for names in name:
#     if names.lower().count('a') == 2:
#         print(names)
#         count +=1
# print(f"Total number of students having two 'a' in their name are :{count}")

# #without using lower or count func
# count_a = 0
# for names in name:
#     for ch in names:
#         if ch =='a' or ch =='A':
#             count_a += 1
# total = 0
# if count_a == 2:
#     total += 1
# print(f"no ofnames :{total}")

#task 3:
count5 = 0
total5 = 0
name = [['Ajay','Priya','Pavan'],['Viru','Raj','Payal'],['Rohan']]
for chotulist in name:
    for nm in chotulist:
        for ch in nm:
            if ch =='a' or ch =='A':
                count5 += 1
            if count5 == 2:
                total5 +=1

print(f"no of names :{total5}")