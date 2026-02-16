class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list[str | None]) -> None:

    for plant in plant_list:
        if plant is None:
            raise InvalidPlant('Error: Cannot water None - invalid plant!')
        else:
            print(f"Watering {plant}")


def test_watering_system() -> None:

    print('Testing normal watering...')
    try:
        print('Opening watering system')
        water_plants(['tomato', 'lettuce', 'carrots'])
        print('Closing watering system (cleanup)')
        print('Watering completed successfully!')
    except InvalidPlant as err:
        print(err)
        print('Closing watering system (cleanup)')

    print('\nTesting with error...')
    try:
        print('Opening watering system')
        water_plants(['tomato', None])
    except InvalidPlant as err:
        print(err)
    finally:
        print('Closing watering system (cleanup)')
        print('\nCleanup always happens, even with errors!')


if __name__ == '__main__':

    print('=== Garden Watering System ===\n')
    test_watering_system()
