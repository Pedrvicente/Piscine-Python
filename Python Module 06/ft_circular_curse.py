from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(
        'validate_ingredients("fire air"): '
        f'{validate_ingredients("fire air")}'
    )
    print(
        'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )
    print()

    print("Testing spell recording with validation:")
    try:
        print(
            'record_spell("Fireball", "fire air"): '
            f'{record_spell("Fireball", "fire air")}'
        )
        print(
            'record_spell("Dark Magic", "shadow"): '
            f'{record_spell("Dark Magic", "shadow")}'
        )
    except Exception as e:
        print(f"Error recording spells: {e}")
    print()

    print("Testing late import technique:")
    try:
        print(
            'record_spell("Lightning", "air"): '
            f'{record_spell("Lightning", "air")}'
        )
    except Exception as e:
        print(f"Error in late import: {e}")
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == '__main__':
    main()
