def mage_counter() -> callable:
    counter_ = 0

    def counter():
        nonlocal counter_
        counter_ += 1
        return counter_
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulate():
        nonlocal total_power
        total_power += initial_power
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str):
        return (f"{enchantment_type} {item_name}")
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print()

    print("Testing enchantment factory...")

    enchant = enchantment_factory('Flaming')
    print(enchant('sword'))

    enchant_2 = enchantment_factory('Frozen')
    print(enchant_2('Shield'))


if __name__ == '__main__':
    main()
