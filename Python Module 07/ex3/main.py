from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print()

    print("Simulating aggressive turn...")

    result = engine.simulate_turn()
    hand_info = [f"{card.name} ({card.cost})" for card in result['hand']]
    print(f"Hand: {hand_info}")

    print()

    print("Turn Execution:")
    print(f"Strategy: {result['strategy']}")
    print(f"Actions: {result['actions']}")

    print()

    print("Game Report:")

    print(engine.get_engine_status())

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == '__main__':
    main()
