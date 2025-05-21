# Inventory Management System
inventory = ["Drinks", "Sweets", "Bread", "Milk", "Wine"]

while True:
    print("\nInventory Menu:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

    selection = input("Enter your  selection (1-4): ")

    if  selection == "1":
        print("Current Inventory:")
        for item in inventory:
            print(f"- {item}")

    elif  selection == "2":
        new_item = input("Enter the item you want to add: ")
        inventory.append(new_item)
        print(f"{new_item} added to inventory.")

    elif  selection == "3":
        removeable_item = input("Enter the item you want to remove: ")
        if  removeable_item in inventory:
            inventory.remove( removeable_item)
            print(f"{ removeable_item} removed from inventory.")
        else:
            print(f"{ removeable_item} not found in inventory.")

    elif  selection == "4":
        print("Exited successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
