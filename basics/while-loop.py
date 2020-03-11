"""
while <condition>:
    # statement 1
    # statement 2
    # ( break )
"""

# 1 to 10 sum
count = 0
val = 1
while val <= 10:
    count += val
    val+=1
print(count)

# menu : DOSA, IDLY, VADA, PONGAL
# If user enters DONE
# Invalid item: item not avaliable or invalid
menu = ["DOSA", "IDLY", "VADA", "PONGAL"]
order = []
while True:
    print("ITEMS AVAILABLE : ", menu)
    item = input("Choose Item : ")
    if item in menu:
        order.append(item)
    elif item == "DONE":
        break
    else:
        print("Item not available or Invalid")
if len(order) == 0:
    print("Your order is empty..")
else:
    print(order)