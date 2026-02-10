def check_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
        if temperature < 0:
            print(f"Error: {temperature} is too cold for plants (min 0°C)")
            return None
        elif temperature > 40:
            print(f"Error: {temperature} is too hot for plants (max 40°C)")
            return None

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    return temperature


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    test_cases = [
        ("25"),
        ("abc"),
        ("100"),
        ("-50"),
    ]

    for test_input in test_cases:
        print(f"Testing temperature: {test_input}")
        result = check_temperature(test_input)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
