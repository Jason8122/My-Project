Menu = ["Pizza","Burger","Pasta"]
print("Welcome to Peniel Restaraunt")
print("Here's the menu")
print("1.Pizza\n2.Burger\n3.Pasta")

Choice = int(input("Please select an order: "))
print("You selected: ", Choice)
if Choice == 1:
  print("You ordered Pizza")
elif Choice == 2:
  print("You ordered Burger")
elif Choice == 3:
  print("You ordered Pasta")
else :
  print("Wrong order not in menu,try again")
if 1<= Choice <= 3:
  add_top = input("Do you want cheese (Yes/No): ")
  if add_top == "Yes":
    print("Cheese coming right away")
  else :
    print("No extra cheese")
print("Your Order is ready and will be served")