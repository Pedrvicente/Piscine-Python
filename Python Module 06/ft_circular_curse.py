import alchemy
import alchemy.grimoire  # noqa: F401
from alchemy.grimoire import validate_ingredients
from alchemy.grimoire import record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print(
        f'validate_ingredients("fire air"): '
        f'{validate_ingredients("fire air")}'
    )
    print(
        f'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )

    print()

    print("Testing spell recording with validation:")
    print(
        f'record_spell("Fireball", "fire air"): '
        f'{record_spell("Fireball", "fire air")}'
    )
    print(
        f'record_spell("Dark magic", "shadow"): '
        f'{record_spell("Dark magic", "shadow")}'
    )

    print()

    print("Testing late import technique:")
    print(
        f'record_spell("Lightning", "air"): '
        f'{record_spell("Lightning", "air")}'
    )

    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == '__main__':
    main()
