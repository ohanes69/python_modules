def create_generator():
    p1: tuple[str | int] = ("alice", 5, "killed monster")
    p2: tuple[str | int] = ("bob", 12, "found treasure")
    p3: tuple[str | int] = ("charlie", 8, "leveled up")

    my_list: list[tuple] = []

    my_list.append(p1)
    my_list.append(p2)
    my_list.append(p3)

    for i in my_list:
        yield i


def event_nb():
    i: int = 0
    while True:
        i += 1
        yield i


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===\n')

    print('Processing 1000 game events...\n')

    my_generator = create_generator()
    nb = event_nb()

    for i in my_generator:
        print(f'Event {next(nb)}: {i}')
