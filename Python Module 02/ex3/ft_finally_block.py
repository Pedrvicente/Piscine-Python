def water_plants(plant_list: list) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_water_plants() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plant_l = ["tomato", "lettuce", "oranges"]
    water_plants(plant_l)
    print()
    print("Testing with error...")
    bad_plants = ["tomato", None, "oranges"]
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_water_plants()
