from ex1.SpellCard import SpellCardClass
from ex1.ArtifactCard import ArtifactCardClass
from ex0.CreatureCard import CreatureCardClass
from ex1.Deck import DeckClass

if __name__ == '__main__':
    print('\n=== DataDeck Deck Builder ===\n')

    print('Building deck with different card types...')

    fire_dragon = CreatureCardClass(
        'Fire Dragon', 5, 'Legendary', 7, 5
    )
    dragon_effect: dict[str] = {'effect': 'Creature summoned to battlefield'}

    mana_crystal = ArtifactCardClass(
        'Mana Crystal', 2, 'Medium', 1, 'Permanent: +1 mana per turn'
    )

    lightning_bolt = SpellCardClass(
        'Lightning Bolt', 3, 'Medium', 'Deal 3 damage to target'
    )

    card_list = [
        fire_dragon,
        mana_crystal,
        lightning_bolt
    ]

    deck = DeckClass()
    deck.add_card(fire_dragon)
    deck.add_card(mana_crystal)
    deck.add_card(lightning_bolt)
    print(f'Deck stats: {deck.get_deck_stats()}')

    print('\nDrawing and playing cards:\n')
    card_drew = deck.draw_card()

    for card in card_list:
        card_drew = deck.draw_card()
        print(f'{card_drew.name} ({card_drew.type})')
        if card_drew.name == 'Fire Dragon':
            print(
                f"Play result: '{card_drew.play(dragon_effect)}\n"
            )
        else:
            print(f'Play result: {card_drew.play({})}\n')

    print('Polymorphism in action: Same interface, different card behaviors!')
