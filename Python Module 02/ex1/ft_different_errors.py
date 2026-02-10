def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden_data = {"tomato": 5, "lettuce": 3}
        garden_data["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    garden_operations()
