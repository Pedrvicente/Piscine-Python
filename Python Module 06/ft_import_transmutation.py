import alchemy
import alchemy.potions
import alchemy.elements
from alchemy.potions import healing_potion as heal


def main() -> None:
    print("=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {alchemy.elements.create_water()}")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print()

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {alchemy.elements.create_earth()}")
    print(f"create_earth(): {alchemy.elements.create_fire()}")
    print(f"create_earth(): {alchemy.potions.strength_potion()}")

    print()

    print("All imports transmutation methods mastered!")


if __name__ == '__main__':
    main()
