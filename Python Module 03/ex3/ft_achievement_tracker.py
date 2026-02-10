if __name__ == '__main__':
    print("=== Achievement Tracker System ===\n")

    alice = ({'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'})
    print(f"Player alice achievements: {alice}")

    bob = ({'first_kill', 'level_10', 'boss_slayer', 'collector'})
    print(f"Player bob achievements: {bob}")

    charlie = ({'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                'perfectionist'})
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===\n")

    unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")

    alice_only = alice - bob - charlie
    bob_only = bob - alice - charlie
    charlie_only = charlie - bob - alice
    rare = alice_only | bob_only | charlie_only
    print(f"Rare achievements (1 player): {rare}\n")

    alice_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob}")
    alice_unique = alice - bob
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob - alice
    print(f"Bob unique: {bob_unique}")
