from ex0.Card import CardClass
from ex2.Combatable import CombatableClass
from ex2.Magical import MagicalClass
from typing import Any


class EliteCardClass(CardClass, CombatableClass, MagicalClass):
    def __init__(self, name: str, cost: int, rarity: str,
                 combat_type: str, attack_power: int,
                 defense_power: int) -> None:
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, target) -> dict:

        attack_dict: dict[Any] = {}
        self.combat_type = 'melee'

        attack_dict = {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': self.combat_type
        }
        return (attack_dict)

    def defend(self, incoming_damage: int) -> dict:

        defend_dict: dict[Any] = {}
        damage_blocked = self.defense_power - incoming_damage

        if damage_blocked < 0:
            damage_blocked = 0
        if damage_blocked > 0:
            still_alive: bool = True
        else:
            still_alive = False

        defend_dict = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': damage_blocked,
            'still_alive': still_alive
        }
        return (defend_dict)

    def get_combat_stats(self) -> dict:

        self.attack_power: int = 5
        arcane_warrior = EliteCardClass(
            'Arcane Warrior', 5, 'Legendary', 'melee', self.attack_power, 7
        )

        return (
            arcane_warrior.attack('Enemy'),
            arcane_warrior.defend(self.attack_power)
        )

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    def play(self, game_state: dict) -> dict:
        pass
