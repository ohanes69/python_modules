class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class GardenManager():
    def __init__(
            self,
            plants_list: list,
            water: int,
            sun: int,
            tank_water: int) -> None:

        self.plants_list: list = plants_list
        self.water: int = water
        self.sun: int = sun
        self.tank_water: int = tank_water

    def add_plants(self) -> None:

        print('Adding plants to garden...')

        for plant in self.plants_list:
            if not plant.strip():
                raise PlantError(
                    'Error adding plant: Plant name cannot be empty!\n'
                )
            else:
                print(f'Added {plant} successfully')

    def watering_plants(self) -> None:

        print('Watering plants...')
        print('Opening watering system')

        for plant in self.plants_list:
            if plant.strip():
                print(f'Watering {plant} - success')

    def check_plants(self) -> None:

        print('Checking plant health...')

        for plant in self.plants_list:
            if self.water > 10:
                raise WaterError(
                    f'Error checking {plant}: '
                    'Water level {self.water} is too high (max 10)\n')
            elif self.water < 1:
                raise WaterError(
                    f'Error checking {plant}: '
                    'Water level {self.water} is too low (min 1)\n')

        for plant in self.plants_list:
            if self.sun > 12:
                raise SunError(
                    f'Error checking {plant}: '
                    'Sun level {self.sun} is too high (max 12)\n')
            elif self.sun < 2:
                raise SunError(
                    f'Error checking {plant}: '
                    'Sun level {self.sun} is too low (min 2)\n')

        for plant in self.plants_list:
            if plant.strip():
                print(
                    f'{plant}: healthy (water: {self.water}, sun: {self.sun})'
                )

    def water_in_tank(self) -> None:

        print('\nTesting error recovery...')
        if self.tank_water < 5:
            raise GardenError('Caught GardenError: Not enough water in tank')


def test_garden_management() -> None:

    plants = GardenManager(['tomato', 'lettuce', ''], 5, 8, 4)

    try:
        plants.add_plants()
    except PlantError as err:
        print(err)

    try:
        plants.watering_plants()
    finally:
        print('Closing watering system (cleanup)\n')

    try:
        plants.check_plants()
    except (WaterError, SunError) as err:
        print(err)

    try:
        plants.water_in_tank()
    except GardenError as err:
        print(err)
    finally:
        print('System recovered and continuing...')


if __name__ == '__main__':

    print('=== Garden Management System ===\n')
    test_garden_management()
    print('\nGarden management system test complete!')
