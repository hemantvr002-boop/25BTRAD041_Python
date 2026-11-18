#===============================================
# UNIT CONVERTER
#===============================================
while True:
    print("===== UNIT CONVERTER =====")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print("Distance in Miles =", round(miles, 2))
    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("Temperature in Fahrenheit =", round(f, 2))
    elif choice == 3:
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print("Weight in Pounds =", round(pounds, 2))
    else:
        print("Invalid Choice!")
        break


#=====================================================
# Bill Generator
#=====================================================
print("=" * 40)
print("           BILL GENERATOR")
print("=" * 40)

items = []
total = 0

while True:
    item = input("\nEnter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Item: Rs "))

    amount = quantity * price
    total += amount

    items.append([item, quantity, price, amount])

    choice = input("\nDo you want to add another item? (yes/no): ").lower()
    if choice != "yes":
        break

gst = total * 0.18
grand_total = total + gst

print("\n" + "=" * 55)
print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Amount"))
print("=" * 55)

for i in items:
    print("{:<20} {:<10} {:<9.2f} {:<9.2f}".format(i[0], i[1], i[2], i[3]))

print("=" * 55)
print(f"Subtotal    : Rs {total:.2f}")
print(f"GST (18%)   : Rs {gst:.2f}")
print(f"Grand Total : Rs {grand_total:.2f}")
print("=" * 55)

paid = float(input("Amount Paid: Rs "))

if paid >= grand_total:
    balance = paid - grand_total
    print(f"Balance Returned: Rs {balance:.2f}")
else:
    due = grand_total - paid
    print(f"Amount Due: Rs {due:.2f}")

print("\nThank you for shopping!")
