#Create a small project in vscode which accepts MRP and discount of a product and display selling 
# price on console.

MRP = float(input("Enter MRP of Product:"))
Discount = float(input("Enter discount % on the product:"))
discount_price = MRP * (Discount/100)
selling_price = MRP - discount_price
print("Selling price of this product is:Rs." ,selling_price)
print("Discount applied:Rs." ,discount_price)