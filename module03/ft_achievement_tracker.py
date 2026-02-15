def compare_common_players(player1: set[str], player2: set[str]) -> set[str]:
    return (player1 & player2)


def compare_unique_players(player1: set[str], player2: set[str]) -> set[str]:
    return (player1 - player2)


def print_achievements(name: str, achievements: set[str]) -> None:
    print(f'Player {name} achievements: {achievements}')


if __name__ == '__main__':
    print('=== Achievement Tracker System ===\n')

    alice: set[str] = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
    }

    bob: set[str] = {
        'first_kill', 'level_10', 'boss_slayer', 'collector',
    }

    charlie: set[str] = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist',
    }

    players = {
        "alice": alice,
        "bob": bob,
        "charlie": charlie,
    }

    for name, ach in players.items():
        print_achievements(name, ach)

    print('\n=== Achievement Analytics ===')

    unique_achievements: set[str] = alice | bob | charlie
    print(f'All unique achievements: {unique_achievements}')
    print(f'Total unique achievements: {len(unique_achievements)}\n')

    common_achievements: set[str] = alice & bob & charlie
    print(f'Common to all players: {common_achievements}')

    alice_rare: set[str] = alice - bob - charlie
    bob_rare: set[str] = bob - alice - charlie
    charlie_rare: set[str] = charlie - alice - bob
    rare_achievements: set[str] = alice_rare | bob_rare | charlie_rare

    print(f'Rare achievements (1 player): {rare_achievements}\n')

    print(f'Alice vs Bob common: {compare_common_players(alice, bob)}')
    print(f'Alice unique: {compare_unique_players(alice, bob)}')
    print(f'Bob unique: {compare_unique_players(bob, alice)}')
