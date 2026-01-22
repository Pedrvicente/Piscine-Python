class Plant:
    """
    class that defines a plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a plant with name, heigth, age"""
        self.name = name
        self.height = height
        self.current_age = age

    def __str__(self) -> str:
        """representation of a plant string"""
        return f"{self.name}: {self.height}cm, {self.current_age} days old"

    def grow(self, amount: int = 1) -> None:
        """grow the plant 1cm at a time"""
        self.height += 1

    def age(self, days: int = 1) -> None:
        """age the plant day by day"""
        self.current_age += 1

    def get_info(self) -> str:
        """get info of the status of the plant"""
        return f"{self.name}: {self.height}cm, {self.current_age} days old"


if __name__ == "__main__":
    garden = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in garden:
        print(f"Created: {plant}")
    print()
    print(f"Total plants created: {len(garden)}")
