"""

Restaurant Billing System

1 - Display the menu with their prices
2 - Take order from the user
3 - If item is invalid throw an error
4 - If user enters done that is order is completed
5 - Show order items and final bill

"""

# define menu
menu = {
    "DOSA": 30,
    "VADA": 10,
    "IDLY": 20,
    "PONGAL": 30
}
order={}
bill=0

def show_menu():
    print("ITEM\t\tPRICE")
    print("-------------------")
    for item in menu.keys():
        print(item, "\t\t", menu[item])

def take_order():
    global bill
    while True:
        item=input("Enter the Items:")
        if item in menu.keys():
            if item in order.keys():
                order[item]=order[item]+1
            else:
                order[item]=1
            bill=bill+menu[item]
        elif item=="DONE":
            break
        else:
            print("Please enter a valid item")
     
def print_order():
    print("Your order is : ")
    for item, item_count in order.items():
        print(item, " - ", item_count)

def print_bill():
    print("Your total bill is : ", bill)

show_menu()
take_order()
print_order()
print_bill()