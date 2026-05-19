#1.Write a program to accept the cost price and selling price find the profit and loss.
# cost_price = float(input("Enter cost price of product:"))
# selling_price = float(input("Enter selling price of product:"))
# if selling_price > cost_price:
#     profit = selling_price - cost_price
#     print(f"profit on this product is {profit}")
# elif selling_price < cost_price:
#      loss =  cost_price - selling_price
#      print(f"loss on this product is {loss}")    
# else:
#      print("neither profit nor loss")


#2.check if the given number is even or odd
# number = int(input("Enter a number:"))
# if number % 2 == 0:
#      print(f"{number} is an even number")
# else:
#      print(f"{number} is an odd number")


#3.check if given number is positive, negative or zero
# number = int(input("Enter a number:"))
# if number > 0:
#     print(f"{number} is a positive number")
# elif number <0 :
#     print(f"{number} is a negative number")
# else:
#     print("given number is zero.")


#4.print number is divisible by 3 and 5 or not
# number = int(input("Enter a number:"))
# if number % 3 ==0 and number % 5 == 0:
#     print(f"{number} is divisible by both 3 and 5")
# else:
#     print(f"{number} is not divisible by both 3 and 5")

#5.swap 2 numbers without using 3rd variable
# number1 = float(input("Enter first number:"))
# number2 = float(input("Enter second number:"))
# print(f"values before swapping {number1} ,{number2}")
# number1 , number2 = number2 , number1
# print(f"values after swapping {number1} ,{number2}")

#6.verify given year is leap year or not
# year = int(input("Enter any year:"))
# if year % 4 ==0 and year % 100 == 0:
#     print("Given year is leap year.")
# else:
#     print("Given year is not leap year.")

#7.find the maximum of given 3 numbers
# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter 2nd number:"))
# num3 = int(input("Enter 3rd number:"))

# if num1 >num2 and num1 > num3:
#     print(f"{num1} is the greatest of all the three given")
# elif num2 >num1 and num2 > num3:
#     print(f"{num2} is the greatest of all the three given")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} is the greatest of all the three given")
# else:
#     print("Wrong data entry!!")

#8.find minimum of given 3 numbers
# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter 2nd number:"))
# num3 = int(input("Enter 3rd number:"))
# if num1 < num2 and num1 < num3:
#     print(f"{num1} is the smallest of all the three given")
# elif num2 < num1 and num2 < num3:
#     print(f"{num2} is the smallest of all the three given")
# elif num3 < num1 and num3 < num2:
#     print(f"{num3} is the smallest of all the three given")
# else:
#     print("Wrong data entry!!")

#9.print sum pf maximum and minimum of 3 numbers
# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter 2nd number:"))
# num3 = int(input("Enter 3rd number:"))
# if num1 < num2 and num1 < num3:
#     minimum = num1
# elif num2 < num1 and num2 < num3:
#     minimum = num2
# else:
#    minimum = num3

# if num1 > num2 and num1 > num3:
#     maximum = num1
# elif num2 > num1 and num2 > num3:
#    maximum = num2
# else:
#     maximum = num3

# print(f"sum of maximum and minimum is {maximum + minimum}")

#10.accept 5 subject marks and print total and per
# sub1 = int(input("Enter marks of subject1:"))
# sub2 = int(input("Enter marks of subject2:"))
# sub3 = int(input("Enter marks of subject3:"))
# sub4 = int(input("Enter marks of subject4:"))
# sub5 = int(input("Enter marks of subject5:"))

# total = sub1 + sub2 +sub3 +sub4 + sub5
# print(f"total of all the subjects is {total}")

# percentage = (total / 500 )*100
# print(f"percentage acquired is {percentage}")