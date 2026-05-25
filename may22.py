# motu_list = [10 , "Rahul" , [45 , "priya" , "Pavan"] , "Kiran" , True]
# print(motu_list[2][1][2])
# for item in motu_list:
#     print(item)

#first way to find sita's index
students_name = ["sai","Rahul","Rohit","sita","gita","Ravi","kumar"]
# print(f"sita's index in list is: {students_name.index("sita")}")

#second way
# l = len(students_name)
# for i in range(0,l):
#         if students_name[i] == "sita":
#                 print(i)
        
#third way
# count = 0
# sita_index = 0
# for ch in students_name:
#         if ch == "sita":
#                 sita_index = count
#         count = count + 1
# print(sita_index)    

#print student whose name is 5 digit and is present at odd index
for i in range(0,len(students_name)):
        if i % 2 != 0:
                if len(students_name[i]) == 5:
                        print(students_name[i])
        

# r = range(5)
# print(r)
# for v in range(100,51,-5):
#         print(v)