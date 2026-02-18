from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list):
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        cards_played = []
        mana_used = 0
        available_mana = 5

        for card in sorted_hand:
            if (mana_used + card.cost <= available_mana
                    and len(cards_played) < len(hand) - 1):
                cards_played.append(card.name)
                mana_used += card.cost

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': mana_used
        }

    def get_strategy_name(self) -> str:
        return f"{type(self).__name__}"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritize = []
        for target in prioritize:
            if target == 'Enemy Player':
                prioritize.insert(0, target)
            else:
                prioritize.append(target)
        return prioritize
