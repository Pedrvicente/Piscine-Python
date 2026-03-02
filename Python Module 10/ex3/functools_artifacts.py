from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        return reduce(operator.add, spells)
    elif operation == 'multiply':
        return reduce(operator.mul, spells)
    elif operation == 'max':
        return max(spells)
    elif operation == 'min':
        return min(spells)
    else:
        return


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(
            base_enchantment, power=50, element='lightning')
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def cast(spell):
        return "Unknown spell type"

    @cast.register(int)
    def _(spell):
        return f"Damage spell: {spell}"

    @cast.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell):
        return f"multi-cast: {spell}"
    return cast


def main() -> None:

    spells = [10, 20, 30, 40]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == '__main__':
    main()
