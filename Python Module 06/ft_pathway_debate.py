import alchemy.transmutation
from alchemy.transmutation import lead_to_gold, stone_to_gem


def main() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")

    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print()

    print("Testing Relative Imports (from advanced.py):")
    print(
        "philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )
    print(
        "exilir_of_life(): "
        f"{alchemy.transmutation.elixir_of_life()}"
    )

    print()

    print("Testing Package Access:")
    try:
        print(
            "alchemy.transmutation.lead_to_gold(): "
            f"{alchemy.transmutation.lead_to_gold()}"
        )
    except AttributeError as e:
        print(f"alchemy.transmutation.lead_to_gold(): AttributeError - {e}")

    try:
        print(
            "alchemy.transmutation.philosophers_stone(): "
            f"{alchemy.transmutation.philosophers_stone()}"
        )
    except AttributeError as e:
        print(
            f"alchemy.transmutation.philosophers_stone(): AttributeError - {e}"
            )

    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == '__main__':
    main()
