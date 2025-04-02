item = input("What item would you like to buy? :")
price= float(input("What is the price of the item? :"))
quantity= int(input("How many would you like? :"))
total = price*quantity
print(f"You have purchased {quantity}x {item} for {total}")