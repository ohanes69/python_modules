def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> str:

    if not plant_name.strip():
        raise ValueError('Error: Plant name cannot be empty!\n')

    if water_level > 10:
        raise ValueError(
            f'Error: Water level {water_level} '
            'is too high (max 10)\n')
    elif water_level < 1:
        raise ValueError(
            f'Error: Water level {water_level} '
            'is too low (min 1)\n')

    if sunlight_hours > 12:
        raise ValueError(
            f'Error: Sunlight hours {sunlight_hours} '
            'is too high (max 12)\n')
    elif sunlight_hours < 2:
        raise ValueError(
            f'Error: Sunlight hours {sunlight_hours} '
            'is too low (min 2)\n')

    return (f'Plant {plant_name} is healthy!\n')


def test_plant_checks() -> None:

    print('Testing good values...')
    try:
        print(check_plant_health('tomato', 5, 5))
    except ValueError as err:
        print(err)

    print('Testing empty plant name...')
    try:
        check_plant_health('', 5, 5)
    except ValueError as err:
        print(err)

    print('Testing bad water level...')
    try:
        check_plant_health('tomato', 12, 5)
    except ValueError as err:
        print(err)

    print('Testing bad sunlight hours...')
    try:
        check_plant_health('tomato', 5, -5)
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    print('=== Garden Plant Health Checker ===\n')
    test_plant_checks()
    print('All error raising tests completed!')
