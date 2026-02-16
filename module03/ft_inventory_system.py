import sys


def nested_dict(inventory: dict[str | int]) -> dict:

    scarce_dict: dict[str | int] = {}
    moderate_dict: dict[str | int] = {}

    key: str
    value: int
    for key, value in inventory.items():
        if value < 5:
            scarce_dict.update({key: value})
        else:
            moderate_dict.update({key: value})

    inventory = {
        "scarce": scarce_dict,
        "moderate": moderate_dict
    }
    return (inventory)


if __name__ == '__main__':
    print('=== Inventory System Analysis ===')
    inventory_list: list[str] = []
    inventory: dict[str | int] = {}

    for i in range(1, len(sys.argv)):
        inventory_list.append(sys.argv[i].split(':'))

    for pair in inventory_list:
        key: str = pair[0]
        value: int = int(pair[1])
        inventory[key] = value

    total_items: int = 0
    for i in inventory.values():
        total_items += int(i)
    type_items: list = inventory.keys()

    print(f'Total items in inventory: {total_items}')
    print(f'Unique item types: {len(type_items)}')

    print('\n=== Current Inventory ===')
    for key, value in inventory.items():
        print(f'{key}: {value} units ({value / total_items * 100:.1f}%)')

    print('\n=== Inventory Statistics ===')
    print(
        f'Most abundant: {max(inventory, key=inventory.get)} '
        f'({inventory[max(inventory, key=inventory.get)]} units)'
    )
    print(
        f'Least abundant: {min(inventory, key=inventory.get)} '
        f'({inventory[min(inventory, key=inventory.get)]} units)'
    )

    print('=== Item Categories ===')
    double_dict: dict[str | int] = nested_dict(inventory)
