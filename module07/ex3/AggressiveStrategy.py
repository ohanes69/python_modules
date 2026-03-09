from ex3.GameStrategy import GameStrategyClass


class AggressiveStrategyClass(GameStrategyClass):

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        mana_available: int = 7
        mana_used: int = 0
        cards_played: list = []
        damage_dealt: int = 0

        for card in sorted_hand:
            if mana_used + card.cost <= mana_available:
                cards_played.append(card.name)
                mana_used += card.cost
                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                else:
                    damage_dealt += card.cost

        targets_attacked = self.prioritize_targets(['Enemy Player'])

        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt,
        }
