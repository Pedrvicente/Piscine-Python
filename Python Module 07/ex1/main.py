from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    new_deck = Deck()
    cards = [
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        ArtifactCard("Mana Crystal", 2, "effect", 3, "+1 mana per turn"),
        SpellCard("Lightning Bolt", 3,
                  "Deal 3 damage to target",
                  "Deal 3 damage to target")
    ]

    for card in cards:
        new_deck.add_card(card)

    print(new_deck.get_deck_stats())

    print()

    print("Drawing and playing cards:\n")

    while new_deck.cards:
        card = new_deck.draw_card()
        print(f"Drew: {card.name} ({type(card).__name__.replace('Card', '')})")
        print(card.play({}))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == '__main__':
    main()
