class WeatherError(Exception):
    pass


class TemperatureTooHighError(WeatherError):
    pass


class TemperatureTooLowError(WeatherError):
    pass


def check_temperature(temp_str: str) -> str:

    try:
        value = int(temp_str)
    except ValueError:
        return (f"Error: '{temp_str}' is not a valid number\n")

    if value > 40:
        raise TemperatureTooHighError(
            f'Error: {value}°C '
            'is too hot for plants (max 40°C)\n')

    if value < 0:
        raise TemperatureTooLowError(
            f'Error: {value}°C '
            'is too cold for plants (min 0°C)\n')

    return (f'Temperature {value}°C is perfect for plants!\n')


def test_temperature_input() -> None:

    print('Testing temperature: 25')
    print(check_temperature('25'))

    print('Testing temperature: abc')
    print(check_temperature('abc'))

    print('Testing temperature: 100')
    try:
        check_temperature('100')
    except TemperatureTooHighError as err:
        print(err)

    print('Testing temperature: -50')
    try:
        check_temperature('-50')
    except TemperatureTooLowError as err:
        print(err)


if __name__ == '__main__':
    print('=== Garden Temperature Checker ===\n')
    test_temperature_input()
    print("All tests completed - program didn't crash!")
