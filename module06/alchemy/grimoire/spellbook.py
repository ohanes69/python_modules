def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.validator import validate_ingredients

    return_output = validate_ingredients(ingredients)
    split_output = return_output.split()

    for output in split_output:
        if output == 'VALID':
            return (
                f'Spell recorded: {spell_name} '
                f'({return_output})'
            )
    return (
        f'Spell rejected: {spell_name} '
        f'({return_output})'
    )
