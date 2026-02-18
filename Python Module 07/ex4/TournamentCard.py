from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
            }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.health, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > damage_taken
        }

    def get_combat_stats(self):
        return {
            'attack': self.attack_power,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        rating = self.rating + (self.wins * 16) - (self.losses * 16)
        return rating

    def update_wins(self, wins: int) -> None:
        self.wins = self.wins + wins

    def update_losses(self, losses: int) -> None:
        self.losses = self.losses + losses

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            'Interfaces': ["Card", "Combatable", "Rankable"],
            'Rating': self.rating,
            'Record': f"{self.wins}-{self.losses}"
        }
