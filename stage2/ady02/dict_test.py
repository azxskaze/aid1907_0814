# def addToInventory(inventory, addedItems):
    # for i in addedItems:
    #     if i in inventory:
    #         inventory[i] = inventory.get(i) + 1
    #     inventory.setdefault(i, 1)
    # return inventory


def displayInventory(dict):
    print('Inventory:')
    count = 0
    for key, value in dict.items():
        count += value
        print(str(value) + "\t" + key)
    print('Total number of items: %d' % count)

def addToInventory(inventory, addedItems):
    # for i in addedItems:
    #     if i in inventory:
    #         inventory[i] = inventory.get(i) + 1
    #     inventory.setdefault(i, 1)
    # return inventory
# def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item] = 1
    return inventory








inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)