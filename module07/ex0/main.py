from Card import CardClass
from CreatureCard import CreatureCardClass

if __name__ == '__main__':

    print('\n=== DataDeck Card Foundation ===\n')
    print('Testing Abstract Base Class Design:\n')

    print('CreatureCard Info:')
    fire_dragon = CreatureCardClass('Fire Dragon', 5, 'Legendary', 7, 5)
    print(fire_dragon.get_card_info())

    print('\nPlaying Fire Dragon with 6 mana available:')
    print(f'Playable: {fire_dragon.is_playable(6)}')

    game_state: dict = {
        'effect': 'Creature summoned to battlefield',
    }
    print(f'Play result: {fire_dragon.play(game_state)}')

    print('\nFire Dragon attacks Goblin Warrior:')
    goblin_warrior = CreatureCardClass('Goblin Warrior', )
