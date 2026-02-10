import time


def generator(num_events):
    players = ['alice', 'bob', 'charlie']
    actions = ['killed monster', 'leveled up', 'found treasure']

    for i in range(num_events):

        h_player = hash((i, 'player'))
        h_level = hash((i, 'level'))
        h_action = hash((i, 'action'))

        player = players[h_player % len(players)]
        action = actions[h_action % len(actions)]
        level = (h_level % 20) + 1

        event = {
            'id': i + 1,
            'player': player,
            'level': level,
            'action': action
        }
        yield event


def high_level(events):
    for event in events:
        if event['level'] > 10:
            yield event


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def primes():
    """Generate prime numbers infinitely"""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


if __name__ == '__main__':
    print(" === Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")

    gen = generator(1000)
    total_count = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    shown = 0
    start_time = time.time()
    for event in gen:
        total_count += 1

        if event['level'] > 10:
            high_level_count += 1

        if event['action'] == 'found treasure':
            treasure_count += 1

        if event['action'] == 'leveled up':
            levelup_count += 1

        if shown < 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
            shown += 1
    print("...")

    print()

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print()
    print("Memory usage: Constant (streaming)")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Processing time: {total_time:.4f} seconds")

    print()
    print("=== Generator Demonstration ===")
    fib = fibonacci()
    fib_list = []
    for i in range(10):
        fib_list.append(next(fib))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_list))}")
    prime_gen = primes()
    prime_list = []
    for i in range(5):
        prime_list.append(next(prime_gen))
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_list))}")
