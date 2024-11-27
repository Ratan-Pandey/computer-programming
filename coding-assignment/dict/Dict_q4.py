 #Check if a Key Exists
inventory = {"apple": 10, "banana": 20, "orange": 15}

key = "apple"
if key in inventory:
    print(f"{key} is available with quantity {inventory[key]}")
else:
    print(f"{key} is not available")
