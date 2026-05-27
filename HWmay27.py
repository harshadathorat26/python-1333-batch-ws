#Task2:smart Electricity bill generator take no of electricity units in input and condition is if units consumption>=300 then extra surcharge of rs.500 otherwise surcharge is rs.100 and print total bill
#bill = rs.units * 8 for units >= 100 and bill =rs. units * 5 for units more than 51 less than 100 and no bill for units < 50 also GST 18 percent
units = int(input("Enter number of electricity units:"))
charge = 0
bill = 0
if units <= 50:
    charge = 0
    bill = 0
elif units <=100:
    bill = 5 * units
    charge = 100
elif units >=101:
    if units >= 300:
        charge = 500
        bill = 8 * units 
    else:
        charge = 100
        bill = units * 8

bill += charge
GST = bill * 0.18
bill += GST 

if units >= 51:
    print(f"\n {'-'*6} {'Smart Electricity bill generator'} {'-'*6} ")
    print(f"|{'units consumption':^17}|{'Extra surcharge':^15}|{'GST':^5}|{'Total Bill':^11}|")
    print(f"|{units:^17}|{charge:^15}|{GST:^5.1f}|{bill:^11}|\n")
else:
    print("No payable bill!!")
