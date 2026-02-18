from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    card = ['play', 'get_card_info', 'is_playable']
    combat = ['attack', 'defend', 'get_combat_stats']
    magical = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print(f"- Card: {card}")
    print(f"- Combatable: {combat}")
    print(f"- Magical: {magical}")

    print()

    print("Playing Arcane Warrior (Elite Card):\n")

    new_card = EliteCard("Arcane Warrior", 5, "spell", 5, 6, 4)
    print("Combat phase:")
    print(f"Attack result: {new_card.attack('Enemy')}")
    print(f"Defend result: {new_card.defend(4)}")

    print()

    print("Magic phase:")
    targets = ['Enemy1', 'Enemy2']
    print(f"Spell cast: {new_card.cast_spell('Fireball', targets)}")
    print(f"Mana channel: {new_card.channel_mana(3)}")

    print()

    print("Multiple interface implementation successful!")


if __name__ == '__main__':
    main()
