if __name__ == '__main__':
    print('=== Game Analytics Dashboard ===\n')

    print('=== List Comprehension Examples ===')
    names_scores: dict[str, int] = {
        'alice': 2300,
        'bob': 1800,
        'charlie': 2150,
        'diana': 2050
    }

    high_scorers: list[str] = []
    high_scorers = [key for key, value in names_scores.items() if value > 2000]
    print(f'High scorers (>2000): {high_scorers}')

    scores_doubled: list[int] = []
    scores_doubled = [value * 2 for key, value in names_scores.items()]
    print(f'Scores doubled: {scores_doubled}')

    is_active: list[str] = []
    is_active = [key for key, value in names_scores.items() if value > 0]
    print(f'Active players: {is_active}')

    print('\n=== Dict Comprehension Examples ===')
    dict_scores: dict[str, int] = {}
    dict_scores = {key: value for key, value in names_scores.items()}
    print(f'Player scores: {dict_scores}')

    print('\n=== Set Comprehension Examples ===')
    unique_players: set[str] = {}
    unique_players = {key for key, value in names_scores.items()}
    print(f'Unique players: {unique_players}')
