Menu = ["Pasta","Burger","Pizza","Soda"]

print("Welcome to Peniel City Covenant Restaraunt")
print("Here's our Menu: ")
print("1.Pasta\n2.Burger\n3.Pizza\n4.Soda")

choice = int(input("What would you like to order: "))
if choice == 1:
    print("You ordered Pasta")
elif choice == 2:
    print("You ordered Burger")
elif choice == 3:
    print("You ordered Pizza")
elif choice == 4:
    print("You ordered Soda")
else:
    print("Invalid choice.Please try again")

if 1<= choice <= 4:
    add_top = input("Do you want cheese('Yes/No')")
    if add_top.lower() == "yes":
        print("Cheese added to your order")
    elif add_top.lower() == "no":
        print("No cheese added to your order")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'")

print("Thank you for your order! Enjoy your meal at Peniel City Covenant Restaraunt.")