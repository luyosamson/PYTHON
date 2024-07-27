def display_menu(products):
    print("Available Products:")
    for i, (product, price) in enumerate(products):
        print(f"{i}. {product}: ${price:.2f}")

def add_to_cart(products, cart):
    while True:
        choice = input("Enter the number of the product to add to cart (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                selected_product = products[choice - 1]
                cart.append(selected_product)
                print(f"{selected_product[0]} added to cart.")
            else:
                print("Invalid choice. Please enter a valid product number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# def calculate_total(cart):
#     total_cost = sum(item[1] for item in cart)
#     return total_cost

# def apply_discount(total_cost):
#     if total_cost > 100:
#         discounted_cost = total_cost * 0.9
#     else:
#         discounted_cost = total_cost
#     return discounted_cost

# def print_receipt(cart, total_cost, discounted_cost):
#     print("\nReceipt:")
#     for product, price in cart:
#         print(f"{product}: ${price:.2f}")
#     print(f"\nTotal Cost before Discount: ${total_cost:.2f}")
#     if discounted_cost < total_cost:
#         print(f"10% Discount Applied! Final Cost: ${discounted_cost:.2f}")
#     else:
#         print("No Discount Applied.")
#     print("Thank you for shopping with us!")

# Sample data
products = [
    ("Apple", 1.99),
    ("Banana", 0.99),
    ("Orange", 2.49),
    ("Milk", 3.49),
    ("Bread", 2.99)
]
r=display_menu(products)
print(r)

# Main program
# def main():
#     cart = []
#     display_menu(products)
#     add_to_cart(products, cart)
#     total_cost = calculate_total(cart)
#     discounted_cost = apply_discount(total_cost)
#     print_receipt(cart, total_cost, discounted_cost)

# if __name__ == "__main__":
#     main()


# Explanation:
# Functions: Each function (display_menu, add_to_cart, calculate_total, apply_discount, print_receipt) encapsulates a specific task related to managing customer orders.
# Lists/Tuples: products is a list of tuples where each tuple contains a product name and its price.
# Conditional Statements: Used in apply_discount to check if the total cost exceeds $100 and apply a discount accordingly.
# Execution Flow: The main function coordinates the execution of the program by calling each function in sequence.
# This program simulates a simplified checkout process for a grocery store, demonstrating the use of conditional statements, functions, and lists/tuples to solve a practical problem. Adjustments can be made to expand functionality or customize the behavior based on specific requirements.