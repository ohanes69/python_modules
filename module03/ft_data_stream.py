import random
import time
from typing import Generator


def count_actions(actions: dict[str, int], action: str) -> None:

    if action == 'killed monster':
        actions['killed monster'] += 1
    if action == 'found treasure':
        actions['found treasure'] += 1
    if action == 'leveled up':
        actions['leveled up'] += 1


def high_level(dict_players: dict[str, int]) -> str:

    high_level_players: int = 0

    for i in dict_players.values():
        if i >= 10:
            high_level_players += 1
    return f'High-level players (10+): {high_level_players}'


def create_generator(
        dict_players: dict[str, int],
        dict_actions: dict[str, int]) -> Generator[str, None, None]:

    for i in range(1, 1001):
        random_player: str = random.choice(list(dict_players.keys()))
        random_action: str = random.choice(list(dict_actions.keys()))
        count_actions(dict_actions, random_action)
        if random_action == 'leveled up':
            dict_players[random_player] += 1
        yield (
            f'Event {i}: Player {random_player} '
            f'(level {dict_players[random_player]}) {random_action}'
        )


def ft_fibonacci_generator(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def ft_is_prime(nb: int) -> bool:
    if nb < 2:
        return False

    for i in range(2, nb):
        if nb % i == 0:
            return False

    return True


def ft_prime_generator(n: int) -> Generator[int, None, None]:
    found: int = 0
    current: int = 2

    while found < n:

        if ft_is_prime(current):
            yield current
            found += 1

        current += 1


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===\n')

    dict_players: dict[str, int] = {
        'alice': 5,
        'bob': 12,
        'charlie': 7,
    }

    dict_actions: dict[str, int] = {
        'killed monster': 0,
        'found treasure': 0,
        'leveled up': 0,
    }

    print('Processing 1000 game events...\n')

    start = time.process_time()

    total_events: int = 0

    for stat in create_generator(dict_players, dict_actions):
        print(stat)
        total_events += 1

    print('\n=== Stream Analytics ===')
    print(f'Total events processed: {total_events}')
    print(high_level(dict_players))

    treasure: int = dict_actions['found treasure']
    level_up: int = dict_actions['leveled up']

    print(f'Treasure events: {treasure}')
    print(f'Level-up events: {level_up}')

    print('\nMemory usage: Constant (streaming)')
    end = time.process_time()
    print(f"Processing time: {end - start:.3f} seconds")

    print('\n=== Generator Demonstration ===')
    n = 10
    fibo_list: list[str] = []

    for number in ft_fibonacci_generator(n):
        fibo_list.append(str(number))

    result = ", ".join(fibo_list)
    print(f'Fibonacci sequence (first {n}): {result}')

    n = 5
    prime_list: list[str] = []

    for number in ft_prime_generator(n):
        prime_list.append(str(number))

    result = ", ".join(prime_list)
    print(f'Prime numbers (first {n}): {result}')
