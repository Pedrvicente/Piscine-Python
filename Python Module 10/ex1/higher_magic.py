def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args):
        result_1 = spell1(*args)
        result_2 = spell2(*args)
        return (result_1, result_2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args):
        result = base_spell(*args)
        return result * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args):
        if condition(*args):
            result = spell(*args)
            return result
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args):
        results = []
        for spell in spells:
            result = spell(*args)
            results.append(result)
        return results
    return sequence


def main() -> None:

    def hit(target):
        return f"Dragon hit {target}"

    def hit_(target):
        return f"Spell hit {target}"

    p = spell_combiner(hit, hit_)
    print("\nTesting spell combiner...")
    print(f"Combined spell result: {', '.join(p('Dragon'))}")

    print()

    def raise_():
        return 10

    power = power_amplifier(raise_, 10)
    print("Testing power amplifier...")
    print(f"Original: {raise_()}, Amplified: {power()}")


if __name__ == '__main__':
    main()


def make_adder(fix: callable) -> callable:
    def add(soma):
        result = soma + fix
        return result
    return add