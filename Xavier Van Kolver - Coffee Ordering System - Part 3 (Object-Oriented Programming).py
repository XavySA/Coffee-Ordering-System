#Brew Haven Coffee Shop - Ordering System (Part 3 - Object-Oriented Programming)
#Author: Xavier Van Kolver

PRICE_PER_COFFEE = 35
 
 
class Order:
    """Represents a single customer's coffee order."""
 
    DISCOUNT_AMOUNT = 10
    DISCOUNT_RATE = 0.10
 
    def __init__(self, customer_name, quantity, price):
        # ----- Attributes -----
        self.customer_name = customer_name
        self.quantity = quantity
        self.price = price
        self.total_cost = 0
        self.discount = 0
        self.amount_payable = 0
 
    def calculate_total(self):
        """Work out the total cost, discount and amount payable for this order."""
        self.total_cost = self.quantity * self.price
 
        if self.quantity >= Order.DISCOUNT_AMOUNT:
            self.discount = self.total_cost * Order.DISCOUNT_RATE
        else:
            self.discount = 0
 
        self.amount_payable = self.total_cost - self.discount
 
    def display_receipt(self):
        """Display a formatted order summary for this order."""
        print("=" * 34)
        print("========= ORDER SUMMARY =========")
        print(f"{'Customer Name'.ljust(17)}: {self.customer_name}")
        print(f"{'Quantity Ordered'.ljust(17)}: {self.quantity}")
        print(f"{'Price per Coffee'.ljust(17)}: R {self.price}")
        print(f"{'Total Cost'.ljust(17)}: R {self.total_cost}")
        print(f"{'Discount'.ljust(17)}: R {self.discount}")
        print(f"{'Amount Payable'.ljust(17)}: R {self.amount_payable}")
        print("=" * 34)
 
 
def main():
    """Repeatedly create and process Order objects until the cashier chooses to stop."""
    processing = True
 
    while processing:
        name = input("Enter customer name: ")
        quantity = int(input("Enter the number of coffees ordered: "))
 
        # Create an Order object for this customer
        order = Order(name, quantity, PRICE_PER_COFFEE)
        order.calculate_total()
        order.display_receipt()
 
        again = input("\nProcess another customer? (Y/N): ")
        if again.upper() != "Y":
            processing = False
 
 
main()
