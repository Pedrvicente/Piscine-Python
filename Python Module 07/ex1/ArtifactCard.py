from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(
            self, name: str,
            cost: int,
            rarity: Rarity,
            durability: int,
            effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}'
        }

    def activate_ability(self) -> dict:
        return {
            'artifact': self.name,
            'effect': self.effect,
            'durability_remaining': self.durability,
            'activated': True
        }
