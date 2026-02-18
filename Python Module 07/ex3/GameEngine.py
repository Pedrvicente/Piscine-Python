from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.damage = 0
        self.cards = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature(),
            self.factory.create_spell(),
            self.factory.create_artifact()
        ]

        battlefield = []

        result = self.strategy.execute_turn(hand, battlefield)

        self.turns += 1
        self.cards += len(hand)
        self.damage += result.get('damage_dealt', 0)

        return {
            'hand': hand,
            'strategy': self.strategy.get_strategy_name(),
            'actions': result
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.damage,
            'cards_created': self.cards
        }
