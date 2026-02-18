from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    new_tour = TournamentPlatform()

    cards = [
        TournamentCard("Fire Dragon", 5, "adeus", 5, 5),
        TournamentCard("Ice Wizard", 5, "adeus", 5, 5)
    ]

    for card in cards:
        id = new_tour.register_card(card)
        stats = card.get_tournament_stats()
        print(f"{card.name} (ID: {id})")
        print(f"- Interfaces: {stats['Interfaces']}")
        print(f"- Rating: {stats['Rating']}")
        print(f"- Record: {stats['Record']}")
        print()

    print("Creating tournament match...")
    match = new_tour.create_match('fire_dragon_001', 'ice_wizard_002')
    print(f"Match: {match}")

    print()

    print("Tournament Leaderboard:")
    new_list = new_tour.get_leaderboard()
    for i, entry in enumerate(new_list, 1):
        name = entry['name']
        rating = entry['rating']
        record = entry['record']
        print(f"{i}. {name} - Rating: {rating} ({record})")

    print()

    print("Platform Report:")

    print(new_tour.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == '__main__':
    main()
