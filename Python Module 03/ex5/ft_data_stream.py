from typing import Generator, Any


def generator(num_events: int) -> Generator[dict[str, Any], None, None]:
    players = ['alice', 'bob', 'charlie']
    actions = ['killed monster', 'leveled up', 'found treasure']

    for i in range(num_events):
        player = players[hash((i, 'player')) % len(players)]
        action = actions[hash((i, 'action')) % len(actions)]
        level = (hash((i, 'level')) % 20) + 1

        yield {
            'id': i + 1,
            'player': player,
            'level': level,
            'action': action
        }


def high_level(
    events: Generator[dict[str, Any], None, None]
) -> Generator[dict[str, Any], None, None]:
    for event in events:
        if event['level'] > 10:
            yield event


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes() -> Generator[int, None, None]:
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main() -> None:
    print(" === Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")

    gen = generator(1000)
    counts = {'total': 0, 'high': 0, 'treasure': 0, 'levelup': 0}
    shown = 0

    for event in gen:
        counts['total'] += 1
        if event['level'] > 10:
            counts['high'] += 1
        if event['action'] == 'found treasure':
            counts['treasure'] += 1
        if event['action'] == 'leveled up':
            counts['levelup'] += 1

        if shown < 3:
            msg = (f"Event {event['id']}: Player {event['player']} "
                   f"(level {event['level']}) {event['action']}")
            print(msg)
            shown += 1

    print("...\n\n=== Stream Analytics ===")
    print(f"Total events processed: {counts['total']}")
    print(f"High-level players (10+): {counts['high']}")
    print(f"Treasure events: {counts['treasure']}")
    print(f"Level-up events: {counts['levelup']}")
    print("\nMemory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")
    fib = fibonacci()
    fib_list = [next(fib) for _ in range(10)]
    print(f"Fibonacci (10): {', '.join(map(str, fib_list))}")

    prime_gen = primes()
    prime_list = [next(prime_gen) for _ in range(5)]
    print(f"Primes (5): {', '.join(map(str, prime_list))}")


if __name__ == '__main__':
    main()
