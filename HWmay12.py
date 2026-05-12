#Task : Design a asystem to check who is older among jay,viru and gabbar
jay = int(input("Enter Jay's age:"))
viru = int(input("Enter viru's age:"))
gabbar = int(input("Enter Gabbar's age:"))

if jay > viru and jay > gabbar:
    print("Jay is older than Viru and Gabbar.")
elif viru > jay and viru > gabbar:
    print("Viru is older than Jay and Gabbar.")
elif gabbar > jay and gabbar > viru:
    print("Gabbar is older than Jay and Viru.")
elif jay == viru == gabbar:
    print("all of them are of same age.")
else:
    print("wrong data entry.")