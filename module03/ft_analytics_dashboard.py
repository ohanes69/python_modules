from typing import Any


def comprehension_list(data: dict[str, dict[str, Any]]) -> None:

    high_scorers: list[str] = [
        x
        for x, obj in data.items()
        if obj['score'] > 2000
    ]
    print(f'High scorers (>2000): {high_scorers}')

    scores_doubled: list[int] = [
        obj['score'] * 2
        for _, obj in data.items()
    ]
    print(f'Scores doubled: {scores_doubled}')

    is_active: list[str] = [
        x
        for x, obj in data.items()
        for y in obj
        if obj[y] is True
    ]
    print(f'Active players: {is_active}')


def comprehension_dict(data: dict[str, dict[str, Any]]) -> None:

    player_scores: dict[str, int] = {
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

    score_categories: dict[str, int] = {
        x: obj for x, obj in categories.items()
    }
    print(f'Score categories: {score_categories}')

    achivement_counts: dict[str, int] = {
        x: len(obj['achievements'])
        for x, obj in data.items()
        for _ in obj
        if obj['active'] is True
    }
    print(f'Achievement counts: {achivement_counts}')


def comprehension_set(data: dict[str, dict[str, Any]]) -> set[str]:

    unique_players: set[str] = {key for key, _ in data.items()}
    print(f'Unique players: {unique_players}')

    all_achievements: list[str] = [
        ach
        for player_data in data.values()
        if 'achievements' in player_data
        for ach in player_data['achievements']
    ]

    unique_achievements: set[str] = {
        ach
        for ach in all_achievements
        if all_achievements.count(ach) == 1
    }
    print(f'Unique achievements: {unique_achievements}')

    regions: set[str] = {
        obj['region']
        for _, obj in data.items()
        for _ in obj
        if obj['active'] is True
    }
    print(f'Active regions: {regions}')
    return (unique_achievements)


if __name__ == '__main__':
    print('=== Game Analytics Dashboard ===\n')

    data: dict[str, dict[str, Any]] = {
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
    comprehension_list(data)

    print('\n=== Dict Comprehension Examples ===')
    comprehension_dict(data)

    print('\n=== Set Comprehension Examples ===')
    unique_achievements_len: set[str] = comprehension_set(data)

    print('\n=== Combined Analysis ===')
    total_players: int = len(data.keys())
    print(f'Total players: {total_players}')

    total_unique_ach: int = len(unique_achievements_len)
    print(f'Total unique achievements: {unique_achievements_len}')

    list_average: list[int] = [
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
