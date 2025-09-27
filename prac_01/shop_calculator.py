"""
This programme gets the number of items and price
of items and calculates its total with
respect to the discount threshold
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    while price_of_item <= 0:
        print("Please enter a valid number")
        price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > DISCOUNT_THRESHOLD:
    total_price = (1 - DISCOUNT_RATE) * total_price
print(f"The total price for {number_of_items} items is ${total_price:.2f}")