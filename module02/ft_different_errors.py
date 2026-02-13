def garden_operations() -> None:

    try:
        print('Testing ValueError...')
        int('abc')
    except ValueError:
        print('Caught ValueError: invalid literal for int()\n')

    try:
        print('Testing ZeroDivisionError...')
        42 / 0
    except ZeroDivisionError:
        print('Caught ZeroDivisionError: division by zero\n')

    try:
        print('Testing FileNotFoundError...')
        with open('missing.txt'):
            pass
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print('Testing KeyError...')
        my_dict = {'car': 'ford'}
        print(my_dict['plant'])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")


def test_error_types() -> None:

    garden_operations()
    try:
        print('Testing multiple errors together...')
        int('abc')
        42 / 0
    except (ValueError, ZeroDivisionError):
        print('Caught an error, but program continues!')

    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    print('=== Garden Error Types Demo ===\n')
    test_error_types()
