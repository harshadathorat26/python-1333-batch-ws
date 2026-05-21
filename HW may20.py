s = "Instagram"
v1 = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
for i in s:
    if i in v1:
        print(i)
        count = count + 1
print(f"Total number of vowels in the string is {count}")
