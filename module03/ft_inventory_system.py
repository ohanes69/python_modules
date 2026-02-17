import sys


class KeyIsDigit(Exception):
    pass


def key_is_digit(key: str) -> None:

    if key.isdigit():
        raise KeyIsDigit('The key is an int, only strings are accepted')


def items_inventory(inventory: dict[str, int]) -> int:
    total_items: int = 0
    for i in inventory.values():
        total_items += int(i)
    type_items: list[str] = list(inventory.keys())

    print(f'Total items in inventory: {total_items}')
    print(f'Unique item types: {len(type_items)}')

    return (total_items)


def current_inventory(inventory: dict[str, int], total_items: int) -> None:
    items = list(inventory.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]

    for key, value in items:
        print(f'{key}: {value} units ({value / total_items * 100:.1f}%)')


def stat_inventory(inventory: dict[str, int]) -> None:

    max_key: str = max(inventory, key=lambda key: inventory[key])
    max_value: int = inventory[max_key]
    min_key: str = min(inventory, key=lambda key: inventory[key])
    min_value: int = inventory[min_key]

    print(f'Most abundant: {max_key} ({max_value} units)')
    print(f'Least abundant: {min_key} ({min_value} units)')


def nested_dict(inventory: dict[str, int]) -> None:

    scarce_dict: dict[str, int] = {}
    moderate_dict: dict[str, int] = {}

    key: str
    value: int
    for key, value in inventory.items():
        if value < 5:
            scarce_dict.update({key: value})
        else:
            moderate_dict.update({key: value})

    nested_inventory: dict[str, dict[str, int]] = {
        "moderate": moderate_dict,
        "scarce": scarce_dict
    }

    for x, obj in nested_inventory.items():
        print(f'{x}: {obj}')


def restock_needed(inventory: dict[str, int]) -> list[str]:
    restock: dict[str, int] = {}

    for key, value in inventory.items():
        if value == 1:
            restock.update({key: value})

    restock_list: list[str] = list(restock)
    return (restock_list)


if __name__ == '__main__':
    print('=== Inventory System Analysis ===')
    inventory_list: list[list[str]] = []
    inventory: dict[str, int] = {}

    if len(sys.argv) == 1:
        print('Required at least 1 argument')
        sys.exit()

    for i in range(1, len(sys.argv)):
        inventory_list.append(sys.argv[i].split(':'))

    for pair in inventory_list:
        try:
            key_is_digit(pair[0])
            key: str = pair[0]
        except KeyIsDigit as err:
            print(err)
            sys.exit()
        try:
            value: int = int(pair[1])
        except ValueError as err:
            print(err)
            sys.exit()

        inventory[key] = value

    total_items = items_inventory(inventory)

    print('\n=== Current Inventory ===')
    current_inventory(inventory, total_items)

    print('\n=== Inventory Statistics ===')
    stat_inventory(inventory)

    print('\n=== Item Categories ===')
    nested_dict(inventory)

    print('\n=== Management Suggestions ===')
    print(f'Restock needed: {restock_needed(inventory)}')

    print('\n=== Dictionary Properties Demo ===')
    print(f'Dictionary keys: {list(inventory.keys())}')
    print(f'Dictionary values: {list(inventory.values())}')

    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
