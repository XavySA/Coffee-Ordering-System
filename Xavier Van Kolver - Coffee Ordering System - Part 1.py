#Brew Haven Coffee Shop - New Ordering System
#Author: Xavier Van Kolver

PRICE_PER_COFFEE = 35.00

#Step 1: Get the customer's name
customer_name = input("Enter customer's name: ")

#Step 2: Get the number of coffees ordered
number_of_coffees = int(input("Enter number of coffees ordered: "))

#Step 3: Calculate the total cost
total_cost = number_of_coffees * PRICE_PER_COFFEE

#Step 4: Apply a 10% discount if 10 or more coffees are ordered
if number_of_coffees >= 10:
    discount_amount = total_cost * 0.10
    final_amount = total_cost - discount_amount
else:
    discount_amount = 0
    final_amount = total_cost
    
#Step 5: Display the order summary:
print("\n----- ORDER SUMMARY -----")
print(f"Customer Name: {customer_name}")
print(f"Number of Coffees Ordered: {number_of_coffees}")
print(f"Total Cost: R{total_cost:.2F}")
print(f"Discount Amount: R{discount_amount:.2f}")
print(f"Final Amount Payable: R{final_amount:.2f}")
