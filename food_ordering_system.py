#define the menu of HOTEL
menu = {
   
    'pizza':90,
    'burger':85,
    'pasta':60,
    'salad':70,
    'coffee':80,
    'maggie':40,
    'sandwich': 70,
    'tea':20,
    'ice cream':40,
    'cakes': 30
}

#greet
print("welcome to Anand Hotel")
print("pizza:90\nburger:85\npasta:60\nsalad:70\ncoffee:80\nmaggie:40\nsandwich:70\ntea:30\nicecream:40\ncakes:30")
  
order_total = 0

item_1 = input("enter the name of item you want to order =")
if item_1 in menu:
   order_total+= menu[item_1]
   
   print(f"your item {item_1} has been added to your order")

else:
  print(f"order item {item_1} is not avaiable yet")

another_order = input("do you want to add another item (yes/no)")
if another_order == "yes":
   item_2 = input("enter the name of second item =")
   if item_2 in menu:
      order_total += menu[item_2]
      print(f"item{item_2} has been added to order")
   else:
      print(f"ordered item {item_2} is  available")

print(f"the total amount of item to pay is :{order_total}")

      


x = "thanks for visiting\n Anand Hotel"
print(x)
    
      
    
      
