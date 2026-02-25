from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str,
                 cost: int,
                 rarity: Rarity,
                 attack: int,
                 health: int,
                 mana: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite creature summoned to battlefield'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = incoming_damage // 2
        damage_taken = incoming_damage - damage_blocked
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'health': self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        total_mana = amount + self.mana
        self.mana = total_mana
        return {
            'channeled': amount,
            'total_mana': total_mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }
