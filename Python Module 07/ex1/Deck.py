from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card = self.cards.pop()
        return card

    def get_deck_stats(self) -> dict:
        creatures = sum(
            1 for card in self.cards if isinstance(card, CreatureCard))
        spells = sum(
            1 for card in self.cards if isinstance(card, SpellCard))
        artifact = sum(
            1 for card in self.cards if isinstance(card, ArtifactCard))

        total = sum(card.cost for card in self.cards)
        average = (
            float(f"{total / len(self.cards):.2f}") if self.cards else 0.0
        )

        return {
            'total_cards': len(self.cards),
            'creatures': (creatures),
            'spells': (spells),
            'artifacts': (artifact),
            'avg_cost': (average)
        }
