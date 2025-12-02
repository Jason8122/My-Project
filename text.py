Menu = {
    "Pizza" : 800,
    "Burger" : 500,
    "Pasta" : 700,
    "Soda" : 150
    
}

print("Welcome to Peniel City covenant Restaurant ")
print("Here's our menu:")
for item, price in Menu.items():
    print(f"{item}: KES {price}")

order_list = []
while True:
    try:
        choice = input("Enter the item you want to order (or type ('Done')to finish): ").title()
        if choice == "Done":
            break
        elif choice not in Menu:
            print("Sorry, we don't have that item. Please choose from the menu.")   
        else:
            quantity = int(input(f"How many {choice}s would you like to order? "))
            if quantity <= 0:
                print("Please enter a valid quantity greater than 0.")
            else:
                order_list.append((choice, quantity,Menu[choice]))
    except ValueError:
        print("Invalid input. Please enter a valid number for quantity or a valid item name.")
    
total = 0
for item,qty, price in order_list:
    total += qty * price
    
if total > 2000:
    discount = total * 0.1
    total -= discount
    print(f"Congratulations! You have received a 10% discount of KES {discount:.2f} on your order.")
print(f"Your total bill is : KES {total:.2f}")

try:
    confirm = input("Confirm your order? (yes/no): ").lower()
    if confirm not in ["yes", "no"]:
        raise ValueError("Please enter 'yes' or 'no'.")
    elif confirm == "yes":
        print("Thank you for your order! Your food will be ready soon.")
    else:
        print("Order cancelled. Thank you for visiting!")
except ValueError as e:
    print("Error:", e)