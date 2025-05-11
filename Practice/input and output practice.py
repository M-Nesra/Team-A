print("Welcome to the store, how can I help you?")
user_name = input("What is your name: ")
item_purchased = int(input("How many items did you purchase: "))

price_item = float(input("What is the price of the item: "))

total_price = item_purchased * price_item

if item_purchased > 5:
    discount = total_price * 0.1
else:
    discount = 0

sales_tax = 0.07 * total_price
final_total = total_price - discount + sales_tax
print (f"sub_price:{total_price}. \nTotal after discount:{discount}. 
       \nSales Tax (7%):{sales_tax}. \nFinal Total:{final_total}.")

print("Thank you fpr shopping with us :)")

  

