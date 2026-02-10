def main() -> None:
    print("=== Game Analytics Dashboard ===")

    players: list[dict] = [
        {
            'name': 'alice', 'score': 2300, 'level': 15,
            'active': True, 'region': 'east'
        },
        {
            'name': 'bob', 'score': 1800, 'level': 12,
            'active': True, 'region': 'north'
        },
        {
            'name': 'charlie', 'score': 2150, 'level': 18,
            'active': True, 'region': 'central'
        },
        {
            'name': 'diana', 'score': 2050, 'level': 14,
            'active': False, 'region': 'north'
        }
    ]

    high_scorers: list[str] = [p['name'] for p in players if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    active_players: list[str] = [p['name'] for p in players if p['active']]
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {
        p['name']: p['score'] for p in players if p['active']
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        'high': len([p for p in players if p['score'] > 2000]),
        'medium': len([p for p in players if 1500 < p['score'] <= 2000]),
        'low': len([p for p in players if p['score'] <= 1500])
    }
    print(f"Score categories: {score_categories}\n")

    print("=== Set Comprehension Examples ===")
    achievements: list[dict] = [
        {'player': 'alice', 'achievement': 'first_kill'},
        {'player': 'bob', 'achievement': 'level_10'},
        {'player': 'alice', 'achievement': 'treasure_hunter'},
        {'player': 'charlie', 'achievement': 'speed_demon'}
    ]

    unique_achievements: set[str] = {a['achievement'] for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    unique_regions: set[str] = {p['region'] for p in players}
    print(f"Active regions: {unique_regions}\n")

    print("=== Combined Analysis ===")
    scores: list[int] = [p['score'] for p in players]
    average: float = sum(scores) / len(scores)
    print(f"Average score: {average:.2f}")

    top: dict = max(players, key=lambda p: p['score'])
    print(f"Top performer: {top['name']} ({top['score']} points)")


if __name__ == '__main__':
    main()
