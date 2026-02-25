from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        name = card.name.lower().replace(' ', '_')
        card_id = f"{name}_{len(self.cards) + 1:03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1
        card_1 = self.cards[card1_id]
        card_2 = self.cards[card2_id]

        if random.choice([True, False]):
            winner = card_1
            winner_id = card1_id
            loser = card_2
            loser_id = card2_id
        else:
            winner = card_2
            winner_id = card2_id
            loser = card_1
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_list = sorted(
            self.cards.items(),
            key=lambda c: c[1].rating,
            reverse=True
        )
        leaderboard = []
        for _, card in sorted_list:
            leaderboard.append({
                'name': card.name,
                'rating': card.rating,
                'record': f"{card.wins}-{card.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = sum(card.rating for card in self.cards.values())
        avg = total / len(self.cards) if self.cards else 0
        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': avg,
            'platform_status': 'active'
        }
