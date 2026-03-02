import time
from functools import wraps


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args):
        start_time = time.time()
        print(f"Casting {func.__name__}...")
        result = func(*args)
        end_time = time.time()
        final_time = end_time - start_time
        print(f"Spell completed in {final_time} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if args[2] >= min_power:
                result = func(*args)
                return result
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for i in range(max_attempts):
                try:
                    return func(*args)
                except Exception:
                    print(
                        f"Spell failed, retrying..."
                        f" (attempt {i+1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not all(c.isalpha() or c == ' ' for c in name):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("\nTesting spell timer...")

    # é a mesma coisa que fireball = spell_timer(fireball)
    @spell_timer
    def fireball():
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print()

    print("\nTesting MageGuild...")
    peter = MageGuild()
    print(peter.validate_mage_name('Peter'))
    print(peter.validate_mage_name('Pe'))
    print(peter.cast_spell('water', 15))


if __name__ == '__main__':
    main()
