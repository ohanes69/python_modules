import sys

if __name__ == '__main__':
    print('=== Player Score Analytics ===')

    if len(sys.argv) < 2:
        print(
            'No scores provided. Usage: python3 ft_score_analytics.py'
            ' <score1> <score2> ...')
        sys.exit()

    scores: list[int] = []
    for i in range(1, len(sys.argv)):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as err:
            print(err)
            sys.exit()
    print(f'Scores processed: {scores}')
    print(f'Total players: {len(scores)}')
    print(f'Total score: {sum(scores)}')
    print(f'Average score: {sum(scores) / len(scores)}')
    print(f'High score: {max(scores)}')
    print(f'Low score: {min(scores)}')
    print(f'Score range: {max(scores) - min(scores)}')
