if __name__ == '__main__':
    print("=== Game Analytics Dashboard ===")

    players = [
        {'name': 'alice', 'score': 2300,
         'level': 15, 'active': True, 'region': 'east'},
        {'name': 'bob', 'score': 1800,
         'level': 12, 'active': True, 'region': 'north'},
        {'name': 'charlie', 'score': 2150,
         'level': 18, 'active': True, 'region': 'central'},
        {'name': 'diana', 'score': 2050,
         'level': 14, 'active': False, 'region': 'north'}
    ]
    high_scores = [p['name'] for p in players if p['score'] > 2000]
    print(f"High scorers (>2000): {high_scores}")

    scores_doubled = [p['score'] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active = [p['name'] for p in players if p['active'] is True]
    print(f"Active players: {active}")

    print()
    print("=== Dict Comprehension Examples ===")

    inventory = {p['name']: p['score'] for p in players if p['active'] is True}
    print(f"Player scores: {inventory}")

    score_categories = {
        'high': len([p for p in players if p['score'] > 2000]),
        'mediam': len([p for p in players
                       if 1500 < p['score'] < 2000]),
        'low': len([p for p in players if p['score'] < 1500])
    }

    print(f"Score categories: {score_categories}")

    achievements = [
        {'player': 'alice', 'achievement': 'first_kill'},
        {'player': 'bob', 'achievement': 'level_10'},
        {'player': 'alice', 'achievement': 'treasure_hunter'},
        {'player': 'charlie', 'achievement': 'speed_demon'},
        {'player': 'alice', 'achievement': 'boss_slayer'},
        {'player': 'charlie', 'achievement': 'collector'},
        {'player': 'bob', 'achievement': 'first_kill'},
        {'player': 'charlie', 'achievement': 'level_10'},
        {'player': 'alice', 'achievement': 'perfectionist'},
        {'player': 'bob', 'achievement': 'treasure_hunter'},
        {'player': 'charlie', 'achievement': 'boss_slayer'},
        {'player': 'alice', 'achievement': 'collector'},
        {'player': 'charlie', 'achievement': 'speed_demon'},
        {'player': 'charlie', 'achievement': 'perfectionist'},
        {'player': 'charlie', 'achievement': 'first_kill'},
    ]

    achievements_count = {}

    for ach in achievements:
        player = ach['player']
        if player in achievements_count:
            achievements_count[player] += 1
        else:
            achievements_count[player] = 1
    print(achievements_count)
    print()

    print("=== Set Comprehension Examples ===")

    unique_players = {p['name'] for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {p['achievement'] for p in achievements}
    print(unique_achievements)

    unique_regions = {p['region'] for p in players}
    print(f"Active regions: {unique_regions}")

    print()

    print("=== Combined Analysis ===")

    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    scores = [p['score'] for p in players]
    average = sum(scores) / len(scores)
    print(f"Average score: {average}")

    top_performer = max(players, key=lambda p: p['score'])
    name = top_performer['name']
    score = top_performer['score']
    print(f"Top performer: {name} ({score} points)")
