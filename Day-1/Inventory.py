def add_item(item, quantity, inventory):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory

def remove_item(item, quantity, inventory):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] <= 0:
            del inventory[item]
    return inventory

inventory = {}
add_item("Apple", 10, inventory)
remove_item("Apple", 5, inventory)
remove_item("Apple", 10, inventory)
print(inventory)



# Bugs
# No validation to check if the quantity to remove is more than available stock.
# If an item reaches zero quantity, 
# it’s removed from the dictionary, but no feedback is given to the user.
