menu_item = ["biryani", "coffe", "tea"]

def menu():
    print("welcome to my selection program")
    print("1 . display menu")
    print("2. add items")
    print("3. remove items from menu")
    print("exit")

    choice = int(input("Enter your choice: "))
    return choice

def display_menu():
    print("*****menu****")
    for index, item in enumerate(menu_item):
        print(index +1, ".", item)

def add_item():

    item = input("Enter the name o the item")
    menu_item.append(item)
    print("Items added:", item)

    def remove_item():
        display_menu()
        item_index = int(input("enter the number of the item: ")) -1
        item = menu_items.pop(item_index)
        print("Item removed, item")


while True:
    choice = menu()
    if choice ==1:
        display_menu()
    elif choice ==2:
        add_item()
    elif choice ==3:
        remove_item()
    elif choice ==4:
        break
    else:
        print("Invalid Choice")

print("Thank You!")