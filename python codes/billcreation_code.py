def get_item_details():
    """Gets item name, price, and quantity from the user."""
    return input("Enter item name: "), float(input("Enter price: ")), int(input("Enter quantity: "))

def calculate_amount(price, quantity):
    """Calculates the amount for a single item."""
    return price * quantity

def print_bill_header():
    """Prints the bill header."""
    print("\n\n\t\t\t MEDICAL STORE BILL")
    print("\t\t\t------------------")
    print("\nSr. No.\tItem Name\t\tPrice\tQuantity\tAmount")
    print("--------------------------------------------------")

def print_bill_footer(total_amount):
    """Prints the bill footer with the total amount."""
    print("--------------------------------------------------")
    print(f"\n\t\t\tTotal Amount: \t\t\t\t\t{total_amount:.2f}")
    print("\t\t\t------------------")

def main():
    """Main function to run the program."""
    bill_items = []
    total_amount = 0

    while True:
        item_name, price, quantity = get_item_details()
        amount = calculate_amount(price, quantity)
        bill_items.append((item_name, price, quantity, amount))
        total_amount += amount

        if input("Do you want to add more items? (y/n): ").lower() != 'y':
            break

    print_bill_header()
    for i, item in enumerate(bill_items, 1):
        print(f"{i}\t\t{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t\t{item[3]:.2f}") 

    print_bill_footer(total_amount)

if __name__ == "__main__":
    main()