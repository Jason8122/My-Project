Menu = ["Pizza","Burger","Pasta"]
print("Welcome to Peniel City Covenant Restaurant")
print("Here's the menu")
print("1.Pizza\n2.Burger\n3.Pasta")

choice = int(input("Please select an order: "))
print("You selected: " , choice)

if choice == 1:
    print("You ordered Pizza")
elif choice == 2:
    print("You ordered Burger")
elif choice == 3:
    print("You ordered Pasta")
else:
    print("Wrong order in menu, try again")

if 1<= choice <= 3:
    add_top = input("Do you want cheese (Yes/No): ")
    if add_top.lower() == "yes":
        print("Cheese added to your order")
    else:
        print("No cheese added to your order")
print("Here's your order")
print("Thank you for dining with us!")    