import math

if __name__ == '__main__':
    print("=== Game Coordinate System ===\n")

    position = (10, 20, 5)
    print(f"Position created: {position}")

    x1, y1, z1 = 0, 0, 0
    x2, y2, z2 = 10, 20, 5
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between ({x1}, {y1}, {z1}) and "
          f"({x2}, {y2}, {z2}): {distance:.2f}\n")

    par_str = "3,4,0"
    new_str = par_str.split(",")
    x = int(new_str[0])
    y = int(new_str[1])
    z = int(new_str[2])
    parsed = (x, y, z)
    print(f"Parsing coordinates: \"{par_str}\"")
    print(f"Parsed position: {parsed}")

    distance_parsed = math.sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2)
    print(f"Distance between ({x1}, {y1}, {z1}) and "
          f"({x}, {y}, {z}): {distance_parsed:.2f}\n")

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    try:
        error_str = "abc,def,ghi".split(",")
        x = int(error_str[0])
        y = int(error_str[1])
        z = int(error_str[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
