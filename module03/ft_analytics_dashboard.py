from collections import Counter

if __name__ == '__main__':
    print('=== Game Analytics Dashboard ===\n')

    data = {
        'alice': {
            'score': 2300,
            'active': True,
            'achievements': [
                "double_kill",
                "double_kill",
                "treasure_hunter",
                "treasure_hunter",
                'first_kill'
            ],
            'region': 'north'
        },
        'bob': {
            'score': 1800,
            'active': True,
            'achievements': [
                "treasure_hunter",
                "treasure_hunter",
                'boss_slayer'
            ],
            'region': 'east'
        },
        'charlie': {
            'score': 2150,
            'active': True,
            'achievements': [
                "double_kill",
                "double_kill",
                "elite_warrior",
                "elite_warrior",
                "quest_master",
                "quest_master",
                'level_10'
            ],
            'region': 'central'
        },
        'diana': {
            'score': 2050,
            'active': False
        },
    }

    print('=== List Comprehension Examples ===')
    high_scorers: list[str] = []
    high_scorers = [
        x
        for x, obj in data.items()
        if obj['score'] > 2000
    ]
    print(f'High scorers (>2000): {high_scorers}')

    scores_doubled: list[int] = []
    scores_doubled = [
        obj['score'] * 2
        for _, obj in data.items()
    ]
    print(f'Scores doubled: {scores_doubled}')

    is_active: list[str] = []
    is_active = [
        x
        for x, obj in data.items()
        for y in obj
        if obj[y] is True
    ]
    print(f'Active players: {is_active}')

    print('\n=== Dict Comprehension Examples ===')
    player_scores: dict[str, int] = {}
    player_scores = {
        x: obj['score']
        for x, obj in data.items()
        for _ in obj
        if obj['active'] is True
    }
    print(f'Player scores: {player_scores}')

    categories: dict[str, int] = {
        'high': 3,
        'medium': 2,
        'low': 1
    }

    score_categories: dict[str, int] = {}
    score_categories = {x: obj for x, obj in categories.items()}
    print(f'Score categories: {score_categories}')

    achivement_counts: dict[str, int] = {}
    achivement_counts = {
        x: len(obj['achievements'])
        for x, obj in data.items()
        for _ in obj
        if obj['active'] is True
    }
    print(f'Achievement counts: {achivement_counts}')

    print('\n=== Set Comprehension Examples ===')

    unique_players: set[str] = set()
    unique_players = {key for key, _ in data.items()}
    print(f'Unique players: {unique_players}')

    unique_achievements: set[str] = set()

    all_achievements = [
        ach
        for player_data in data.values()
        if 'achievements' in player_data
        for ach in player_data['achievements']
    ]

    counts = Counter(all_achievements)
    unique_achievements = {ach for ach, count in counts.items() if count == 1}
    print(f'Unique achievements: {unique_achievements}')

    regions: set[str] = set()
    regions = {
        obj['region']
        for _, obj in data.items()
        for _ in obj
        if obj['active'] is True
    }
    print(f'Active regions: {regions}')

    print('\n=== Combined Analysis ===')
    total_players: int = len(data.keys())
    print(f'Total players: {total_players}')

    total_unique_ach: int = len(unique_achievements)
    print(f'Total unique achievements: {total_unique_ach}')

    list_average: list[int]

    list_average = [
        obj['score']
        for _, obj in data.items()
    ]

    print(f'Average score: {sum(list_average) / total_players}')

    max_score: int = max(list_average)

    name_top_performer: str = [
        x
        for x, obj in data.items()
        if obj['score'] == max_score][0]

    len_achievement: int = [
        len(obj['achievements'])
        for x, obj in data.items()
        if obj['score'] == max_score][0]

    print(
        f'Top performer: {name_top_performer} '
        f'({max_score} points, {len_achievement} achievements)'
    )
