""" This script shows a basic python program
that shows information relative to a plant """


def main() -> None:
    """main function that stores and shows the plant data"""
    plant_name: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
