from alchemy.grimoire.validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    x = result.split()

    for y in x:
        if y == 'VALID':
            return (f'Spell recorded: {spell_name} ({validate_ingredients(ingredients)})')
    return (f'Spell rejected: {spell_name} ({validate_ingredients(ingredients)})')


# if __name__ == '__main__':
#     print()