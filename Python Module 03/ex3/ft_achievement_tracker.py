def main() -> None:
    """Gere as conquistas usando sets com type hints."""
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
    }
    bob: set[str] = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
    }
    charlie: set[str] = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===\n")

    unique: set[str] = alice | bob | charlie
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    common: set[str] = alice & bob & charlie
    print(f"Common to all players: {common}\n")

    rare: set[str] = (
        (alice - bob - charlie) |
        (bob - alice - charlie) |
        (charlie - bob - alice)
    )
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == '__main__':
    main()
