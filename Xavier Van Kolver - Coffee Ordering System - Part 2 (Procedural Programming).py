#Brew Haven Coffee Shop - Ordering System (Part 2 - Procedural Programming)
#Author: Xavier Van Kolver

#Constants:
PRICE_PER_COFFEE = 35
DISCOUNT_AMOUNT = 10
DISCOUNT_RATE = 0.10

def capture_order():
    """Ask the cashier for the customer's name and number of coffees ordered."""
    name = input("Enter the customer's name: ")
    quantity = int(input("Enter the number of coffees ordered: "))
    return name, quantity

def calculate_total(quantity):
    """Calculate the total cost, discount and amount payable for a given quantity."""
    total_cost = quantity * PRICE_PER_COFFEE
    
    if quantity >= DISCOUNT_AMOUNT:
        discount = total_cost * DISCOUNT_RATE
    else:
        discount = 0
        
    amount_payable = total_cost - discount
    return total_cost, discount, amount_payable

def display_receipt(name, quantity, total):
    """Display a formatted order summary. 'total' is the tuple from calculate_total()."""
    total_cost, discount, amount_payable = total
    
    print("=" * 34)
    print("===== ORDER SUMMARY =====")
    print(f"{'Customer Name'.ljust(17)}: {name}")
    print(f"{'Quantity Ordered'.ljust(17)}: {quantity}")
    print(f"{'Price per Coffee'.ljust(17)}: R {PRICE_PER_COFFEE}")
    print(f"{'Total Cost'.ljust(17)}: R {total_cost}")
    print(f"{'Discount'.ljust(17)}: R {discount}")
    print(f"{'Amount Payable'.ljust(17)}: R {amount_payable}")
    print("=" * 34)
    
def main():
    """Repeatedly process customer orders until the cashier chooses to stop."""
    processing = True
    
    while processing:
        name, quantity = capture_order()
        total = calculate_total(quantity)
        display_receipt(name, quantity, total)
        
        again = input("\nProcess another customer? (Y/N): ")
        if again.upper() != "Y":
            processing = False

main()
    