#Task: Design a portal for pune RTO.-check user's age for eligibility.
#user age should be above 18 and below 75 then eligible for applying RTO licence
# if less then display wait for ... years
# and if age is above 75 then display you are age bar otherwise welcome to pune RTO portal


age = int(input("Enter your age:"))
if age > 0:
    if age >18 and age < 75:
        print("You are eligible for applying for RTO license.")
    elif age < 18 :
        print(f"wait for {18-age} years.")
    else :
        print("you are age bar.")

