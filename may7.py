r = 2
n = "harshada"
per = 90.525491

# #d is for decimal numbers and .2f is for deciding how many numbers after decimal point
# s = f"student roll is {r:03d} , name is {n}, percentage is {per:.2f}"
# print(s)

# #trying to arrange data into a table
# print("-" * 25)
# print("|Roll |Name | Percentage")
# print("-" * 25)
# print(f"|{r:^5} |{n:^5}| {per:^11}")
# #here we can use < for left alignment and > for right alignment and ^ for center alignment
# print("-" * 25)

# #using .format()
# s1 = "student roll is {} , name is {}, percentage is {}".format(r,n,per)
# s2 = "student roll is {0} , name is {1}, percentage is {2}".format(r,n,per)
# s3 = "student roll is {v1} , name is {v2}, percentage is {v3}".format(v1=r,v2=n,v3=per)
# print(s1,s2,s3)

#using %
s4 = "student roll number is %d , name is %s , percentage is %f"%(r,n,per)
print(s4)