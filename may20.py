# s = "instagram"
# print(s.startswith("in"))
# print(s.isalnum())
# count = 0
# for ch in s:
#     count += 1
#     print(count)
# s = "Instragram"
# count = 0
# for ch in s:
#     print(count)
#     count += 1
# for i in s:
#     print(i)

# s = input("Enter a string: ")
# count=0
# v1 = input("Enter the character you want to find:")
# for i in s:
#     if i ==v1:
#         count= count +1
# print(f"the count of {v1} is {count}")

s = "I Love Python Programming"
count = 0
for i in s:
    if i == " ":
        count = count +1
print(f"the count of total white spaces is {count}")

