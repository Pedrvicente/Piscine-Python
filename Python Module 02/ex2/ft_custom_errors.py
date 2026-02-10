class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    try:
        check_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
