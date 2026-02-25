from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    print(dragon.get_card_info())

    print()

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
