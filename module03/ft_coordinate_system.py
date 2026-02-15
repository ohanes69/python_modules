import sys
import math


def print_error(err: ValueError, value: str) -> None:
    print(f'Parsing invalid coordinates: "{value}"')
    print(f'Error parsing coordinates: {err}')
    print(f'Error details - Type: {type(err).__name__}, Args: {err}')
    sys.exit()


def len_is_not_3() -> None:
    print("Error: exactly 3 coordinates required.")
    sys.exit()


if __name__ == '__main__':
    print('=== Game Coordinate System ===\n')

    if (len(sys.argv) < 2):
        print('No arguments provided.')
        sys.exit()

    list_argv: list[int] = []
    split_argv: list[str] = []

    if (len(sys.argv) == 2):
        split_argv = sys.argv[1].split(',')
        if len(split_argv) != 3:
            len_is_not_3()
        for i in range(len(split_argv)):
            try:
                list_argv.append(int(split_argv[i]))
            except ValueError as err:
                print_error(err, split_argv[i])

    else:
        if len(sys.argv) - 1 != 3:
            len_is_not_3()
        for i in range(1, len(sys.argv)):
            try:
                list_argv.append(int(sys.argv[i]))
            except ValueError as err:
                print_error(err, sys.argv[i])

    position: tuple[int, ...] = tuple(list_argv)
    position_zero: tuple[int, ...] = (0, 0, 0)

    x1, y1, z1 = position_zero
    x2, y2, z2 = position

    distance: float = math.sqrt(
        pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2)
    )

    print(f'Position created: {position}')
    print(f'Distance between {position_zero} and {position}: {distance:.2f}\n')

    print('Unpacking demonstration:')
    print(f'Player at x={x2}, y={y2}, z={z2}')
    print(f'Coordinates: x={x2}, y={y2}, z={z2}')
