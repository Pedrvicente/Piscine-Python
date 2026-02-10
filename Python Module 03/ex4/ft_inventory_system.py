import sys

if __name__ == '__main__':
    print("=== Inventory System Analysis ===")

    inventory = {}
    try:
        for arg in sys.argv[1:]:
            parts = arg.split(":")
            name = parts[0]
            quantity = int(parts[1])
            inventory[name] = quantity
    except (ValueError, IndexError):
        print(f"Error: Invalid format '{arg}'. Use item:quantity")

    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory)}")

    print()

    print("=== Current Inventory ===")
    total = sum(inventory.values())
    sorted_dic = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for name, quantity in sorted_dic:
        average = (quantity / total) * 100
        print(f"{name}: {quantity} units ({average:.1f}%)")

    print()

    print("=== Inventory Statistics ===")
    get_type = max(inventory, key=inventory.get)
    biggest = inventory[get_type]
    print(f"Most abundant: {get_type} ({biggest} units)")
    get_type_min = min(inventory, key=inventory.get)
    smallest = inventory[get_type_min]
    print(f"Least abundant: {get_type_min} ({smallest} units)")

    print()

    moderate = {}
    scarce = {}

    for name, quantity in inventory.items():
        if quantity < 5:
            scarce[name] = quantity
        else:
            moderate[name] = quantity

    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print()

    print("=== Management Suggestions ===")
    low_stock = {}
    for name, quantity in scarce.items():
        if quantity < 2:
            low_stock[name] = quantity
    restock = list(low_stock)
    print(f"Restock needed: {restock}")

    print()

    print("=== Dictionary Properties Demo ===")
    keys = list(inventory.keys())
    print(f"Dictionary keys: {keys}")
    values = list(inventory.values())
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
