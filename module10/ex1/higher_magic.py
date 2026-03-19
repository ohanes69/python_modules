def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        s1, s2 = spell1(*args, **kwargs), spell2(*args, **kwargs)
        return (f"Combined spell result: {s1}, {s2}")

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args, **kwargs):
        original = base_spell(*args, **kwargs)
        amplified = original * multiplier
        return (f"Original: {original}, Amplified: {amplified}")

    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


def main() -> None:
    print('Testing spell combiner...\n')

    def spell1():
        return "Fireball hits Dragon"

    def spell2():
        return "Heals Dragon"

    sc = spell_combiner(spell1, spell2)
    print(sc())

    print('\nTesting power amplifier...\n')

    def base_spell():
        return (5)

    pa = power_amplifier(base_spell, 10)
    print(pa())


if __name__ == '__main__':
    main()
