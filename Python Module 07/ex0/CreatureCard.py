from ex0.Card import Card
from ex0.Card import Rarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        if attack > 0 and health > 0:
            self.attack = attack
            self.health = health
        else:
            raise ValueError("Only positive numbers")

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
            }

    def attack_target(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity.value,
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }
