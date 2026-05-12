# expr = "20+45+7/5"

# res = eval(expr)
# print(res)

# v1 = eval(input("Enter a number:"))
# print("you entered:" , v1)
# print("type of v1:", type(v1))

MRP = eval(input("Enter MRP of Product:"))
Discount = eval(input("Enter discount % on the product:"))
discount_price = MRP * (Discount/100)
selling_price = MRP - discount_price
print("Selling price of this product is:Rs." ,selling_price)
print("Discount applied:Rs." ,discount_price)