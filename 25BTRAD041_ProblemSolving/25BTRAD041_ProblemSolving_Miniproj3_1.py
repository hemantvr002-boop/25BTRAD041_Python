
# Sales Data Analyzer

sales = {}

def add_product():
    name = input("Enter product name: ")

    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per unit: "))

    if quantity < 0 or price < 0:
        print("Quantity and price cannot be negative!")
        return

    if name in sales:
        sales[name]["quantity"] += quantity
        sales[name]["price"] = price
        print("Product sales updated successfully!")
    else:
        sales[name] = {
            "quantity": quantity,
            "price": price
        }
        print("Product added successfully!")

def display_sales():
    if not sales:
        print("No sales records found.")
        return

    print("\n------- SALES REPORT -------")

    for name, details in sales.items():
        revenue = details["quantity"] * details["price"]

        print("\nProduct:", name)
        print("Quantity Sold:", details["quantity"])
        print("Price:", details["price"])
        print("Revenue:", revenue)

def total_sales():
    total = 0

    for details in sales.values():
        total += details["quantity"] * details["price"]

    print("\nTotal Sales Revenue:", total)

def highest_selling():
    if not sales:
        print("No sales records found.")
        return

    product = max(
        sales,
        key=lambda name: sales[name]["quantity"]
    )

    print("\nHighest Selling Product:", product)
    print("Quantity Sold:", sales[product]["quantity"])

def compare_products():
    if not sales:
        print("No sales records found.")
        return

    print("\n----- PRODUCT PERFORMANCE -----")

    for name, details in sales.items():
        revenue = details["quantity"] * details["price"]

        print(name, "-> Revenue:", revenue)

# Main Menu
while True:
    print("\n===== SALES DATA ANALYZER =====")
    print("1. Add Product")
    print("2. Display Sales")
    print("3. Calculate Total Sales")
    print("4. Highest Selling Product")
    print("5. Compare Product Performance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        display_sales()
    elif choice == "3":
        total_sales()
    elif choice == "4":
        highest_selling()
    elif choice == "5":
        compare_products()
    elif choice == "6":
        print("Exiting Sales Data Analyzer...")
        break
    else:
        print("Invalid choice! Try again.")
