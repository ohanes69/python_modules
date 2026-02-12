class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def is_wilting(age: int) -> None:
    if age > 10:
        raise PlantError("Caught PlantError: The tomato plant is wilting!")


def is_enough_water(liters: int) -> None:
    if liters < 5:
        raise WaterError("Caught WaterError: Not enough water in the tank!")


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===\n')

    print('Testing PlantError...')
    try:
        is_wilting(12)
    except PlantError as err:
        print(err)

    print('\nTesting WaterError...')
    try:
        is_enough_water(4)
    except WaterError as err:
        print(err)

    print("\nTesting catching all garden errors...")
    try:
        is_wilting(12)
    except GardenError as err:
        print(err)
    try:
        is_enough_water(4)
    except GardenError as err:
        print(err)
    print("\nAll custom error types work correctly!")
