def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_p = min(mages, key=lambda x: x['power'])['power']
    total = sum(list(map(lambda x: x['power'], mages)))
    size = len(mages)
    avg = round(total / size, 2)

    return {
        'max_power': max_power,
        'min_power': min_p,
        'avg_power': avg
    }


def main() -> None:

    artifacts = [
        {'name': 'Crystal Orb', 'power': 105, 'type': 'art'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'art'},
    ]
    print("Testing artifact sorter...")
    sorted_list = artifact_sorter(artifacts)
    first = sorted_list[0]
    second = sorted_list[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print()

    print("Testing spell transformer...")

    spells = ['fire', 'water', 'rage']

    trans_list = spell_transformer(spells)
    print(' '.join(trans_list))


if __name__ == '__main__':
    main()
