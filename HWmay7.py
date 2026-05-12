name = input("Enter your name:")
age = eval(input("Enter your age:"))
addr = input("Enter your address:")
email = input("Enter your email id:")

print("-"*20)
print("|Name|Age|Address|Email|")
print("-"*20)
print(f"|{name}|{age:02d}|{addr}|{email}|")
print("-"*20)

s = "my name is {}, my age is {}, my address is {} and my email id is {}".format(name,age,addr,email)
print(s)